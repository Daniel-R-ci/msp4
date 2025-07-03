from django.urls import path
from . import views

urlpatterns = [
   path('request_name/', views.request_name, name='request_name'),
]
