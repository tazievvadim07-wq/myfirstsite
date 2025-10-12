from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),   # подключаем main
    path('blog/', include('blog.urls')),  # подключаем blog
]

