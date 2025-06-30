from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'publish_on', 'updated_on')
    ordering = ['published', '-publish_on', 'updated_on']
