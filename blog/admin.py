from django.contrib import admin
from .models import Author, Article, Tag


# 👇 Этот класс позволяет видеть статьи прямо в карточке автора
class ArticleInline(admin.TabularInline):
    model = Article
    extra = 1  # сколько пустых строк для добавления новых статей


# 👇 Настраиваем отображение автора в админке
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    inlines = [ArticleInline]  # добавляем статьи внутрь карточки автора


# 👇 Настраиваем отображение статьи в админке
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_filter = ("author",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)



