from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.students_view, name="students"),
   path('feedback/', views.feedback, name='feedback'),
]