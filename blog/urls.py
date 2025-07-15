from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog_list, name='blog'),
   path('<int:article_id>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_article_comment'), # noqa
   path('<int:article_id>/edit_comment/<int:comment_id>', views.edit_comment, name="article_comment_edit"), # noqa
   path('<int:article_id>', views.blog_detail, name='blog_post')
]
