from django.contrib import admin
from .models import Article, Article_Comment

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'publish_on', 'updated_on']
    ordering = ['published', '-publish_on', 'updated_on']


@admin.register(Article_Comment)
class Article_CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'posted_on', 'visible')
    ordering = ['posted_on',]
