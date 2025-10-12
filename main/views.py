from django.http import HttpResponse

def about(request):
    return HttpResponse("Обо мне: Глупенький студент, не разбираюсь в джанго")

def home(request):
    return HttpResponse("Главная страница моего сайта")

