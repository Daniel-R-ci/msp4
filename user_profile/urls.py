from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('request_name/', views.request_name, name='request_name'),
]
