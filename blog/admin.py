from django.contrib import admin
from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "content")

admin.site.register(Category)

