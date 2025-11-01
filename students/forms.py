from django import forms
from django.core.exceptions import ValidationError
from .models import Student

# Обычная форма (forms.Form) с валидацией на уровне полей
class StudentForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        max_length=100,
        label="Имя",
        widget=forms.TextInput(attrs={'placeholder': 'Иван'})
    )
    age = forms.IntegerField(
        label="Возраст",
        min_value=0,  # основная логика в clean_age
    )
    email = forms.EmailField(label="Email")
    group = forms.CharField(max_length=50, label="Группа")

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            return age
        if age < 16:
            raise ValidationError("Возраст должен быть не менее 16 лет")
        return age

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and any(ch.isdigit() for ch in name):
            raise ValidationError("Имя не должно содержать цифры")
        return name

# ModelForm, связанная с моделью Student
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'group']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Иван'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ivan@example.com'}),
            'group': forms.TextInput(attrs={'placeholder': 'IT-101'}),
        }
        labels = {
            'name': 'Имя',
            'age': 'Возраст',
            'email': 'Email',
            'group': 'Группа',
        }

    # поле-валидации тоже можно реализовать отдельно
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and any(ch.isdigit() for ch in name):
            raise ValidationError("Имя не должно содержать цифры")
        if name and len(name) < 2:
            raise ValidationError("Имя должно быть не короче 2 символов")
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            return age
        if age < 16:
            raise ValidationError("Возраст должен быть не менее 16 лет")
        return age

    # Метод clean() для проверки нескольких полей вместе
    def clean(self):
        cleaned_data = super().clean()
        group = cleaned_data.get('group')
        age = cleaned_data.get('age')

        # проверка group: должно начинаться с "IT-"
        if group:
            if not group.startswith("IT-"):
                # привязываем ошибку к полю group
                self.add_error('group', "Группа должна начинаться с IT-")

        # проверка возраста: если > 40 — выдаём ошибку (привязанную к age)
        if age is not None:
            if age > 40:
                self.add_error('age', "Слишком взрослый студент для этой группы!")
