from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # / → функция
    path('contact/', views.ContactView.as_view(), name='contact'),  # /contact → класс
    path('hello/', views.HelloView.as_view(), name='hello'),        # /hello?name=Имя
]

