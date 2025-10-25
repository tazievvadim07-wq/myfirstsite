from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Book

def students_view(request):
    students = [
        {"name": "Айжан", "age": 19, "group": "IT-23A"},
        {"name": "Мансур", "age": 20, "group": "IT-23A"},
        {"name": "Алихан", "age": 18, "group": "IT-23B"},
    ]

    group_info = {"name": "IT-23A", "specialty": "Веб-разработка", "year": 2025}

    context = {
        "students": students,
        "group_info": group_info
    }

    return render(request, "main/students.html", context)

def feedback(request):
   result = None
   if request.method == "POST":
       name = request.POST.get("name")
       message = request.POST.get("message")
       if name== "" and message =="":
           result = "Ошибка, все поля должны быть заполнены"
       else:
           result = f"Спасибо, {name}! Мы получили твоё сообщение: {message}"

   return render(request, "main/form.html", {"result": result})


def article_detail(request, id):
   return HttpResponse(f"Вы просматриваете статью с ID = {id}")

def user_detail(request, id):
    return HttpResponse (f"Профиль пользователя {id}")

articles = [
   {"id": 1, "title": "Django основы"},
   {"id": 2, "title": "Шаблоны в Django"},
   {"id": 3, "title": "ORM и базы данных"}
]

def article_detail_1(request, id):
   article = next((a for a in articles if a["id"] == id), None)
   if article:
       return HttpResponse(f"Статья: {article['title']}")
   else:
       return HttpResponse("Статья не найдена")
   
def home(request):   
    return HttpResponse("Главная страница")



def search_view(request):
    query = request.GET.get('q')  # получаем введённый текст из формы
    results = []

    if query:
        results = Book.objects.filter(author__icontains=query)  # ищем по части имени автора (без учёта регистра)

    context = {
        'query': query,
        'results': results
    }
    return render(request, 'main/search.html', context)