from django.shortcuts import render

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