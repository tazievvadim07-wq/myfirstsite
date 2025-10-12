from django.http import HttpResponse

def index(request):
    return HttpResponse("Это блог-раздел моего сайта")

