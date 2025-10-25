from django.db import models

class Author(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField(unique=True)

   def __str__(self):
       return self.name


class Tag(models.Model):
   name = models.CharField(max_length=30, unique=True)

   def __str__(self):
       return self.name


class Article(models.Model):
   title = models.CharField(max_length=100)
   content = models.TextField()
   author = models.ForeignKey(Author, on_delete=models.CASCADE)
   tags = models.ManyToManyField(Tag)  # связь многие ко многим
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.title
   

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
