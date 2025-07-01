from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog_list, name='blog'),
   path('post/<int:article_id>', views.blog_detail, name='blog_post')
]
