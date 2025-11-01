from django.contrib import admin
from django.urls import path, include
from blog.views import articles_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  
    path('blog/', include('blog.urls')),
    path('search/', include('blog.urls')),
    path('students/', include('students.urls')),  # Добавляем маршруты приложения students
    path('articles/', articles_view, name='articles'),  # Добавляем маршруты приложения articles
]

