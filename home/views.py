from django.shortcuts import render
from django.conf import settings

# Create your views here.


def home_view(request):
    return render(request, 'home/index.html',)
