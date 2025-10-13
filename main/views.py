<<<<<<< HEAD
from django.shortcuts import render

def home_view(request):
    return render(request, 'main/home.html')

def news_view(request):
    news = [
        {"title": "Django 5.0 вышел!", "text": "Вышла новая версия Django."},
        {"title": "Python 3.13", "text": "Добавлены новые возможности!"},
    ]
    return render(request, 'news.html', {'news': news})
=======
from django.http import HttpResponse
from django.views import View

# 👇 Функциональное представление
def home(request):
    return HttpResponse("Главная страница моего сайта")

# 👇 Классовое представление
class ContactView(View):
    def get(self, request):
        return HttpResponse("Свяжитесь со мной!")

# 👇 Класс с параметром из строки запроса
class HelloView(View):
    def get(self, request):
        # получаем значение "name" из запроса, если его нет — используем "гость"
        name = request.GET.get("name", "гость")
        return HttpResponse(f"Привет, {name}!")
>>>>>>> 71c6a63a36fbb88984bbb5781bbbf25bd86b63b2
