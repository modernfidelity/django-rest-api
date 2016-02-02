from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "strapline", "picture")


admin.site.register(Article, ArticleAdmin)
