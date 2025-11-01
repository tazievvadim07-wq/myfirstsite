from django.shortcuts import render, redirect
from .forms import StudentModelForm, StudentForm

def student_form_view(request):
    """
    Показываем и валидируем StudentModelForm.
    При успешной отправке сохраняем модель и показываем сообщение.
    """
    success = False

    if request.method == "POST":
        # используем ModelForm (можно заменить на StudentForm при необходимости)
        form = StudentModelForm(request.POST)
        if form.is_valid():
            # сохраняем модель в БД
            form.save()
            success = True
            # Можно сделать redirect на 'success' страницу, но по условию — показать сообщение на той же странице
            # Если хотим очистить форму после успешной отправки:
            form = StudentModelForm()
    else:
        form = StudentModelForm()

    return render(request, "students/student_form.html", {"form": form, "success": success})

