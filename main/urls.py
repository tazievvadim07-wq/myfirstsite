from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.students_view, name="students"),
   path('feedback/', views.feedback, name='feedback'),
    path('articles/<int:id>/', views.article_detail, name="articles"),
    path('user/<str:id>/', views.user_detail, name="user"),
    path('article/<int:id>/', views.article_detail_1, name="article1"),
    path('', views.home, name='home'),
    path('search/', views.search_view, name='search'),
]