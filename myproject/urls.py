from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  
    path('blog/', include('blog.urls')),
    path('search/', include('blog.urls')),
    path('students/', include('students.urls')),  # Добавляем маршруты приложения students
]

