from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    group = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.group})"

