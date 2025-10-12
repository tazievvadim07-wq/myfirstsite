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
