from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home_view, name='home'),
    path('news/', views.news_view, name='news'),
]
=======
    path('', views.home, name='home'),                    # / → функция
    path('contact/', views.ContactView.as_view(), name='contact'),  # /contact → класс
    path('hello/', views.HelloView.as_view(), name='hello'),        # /hello?name=Имя
]

>>>>>>> 71c6a63a36fbb88984bbb5781bbbf25bd86b63b2
