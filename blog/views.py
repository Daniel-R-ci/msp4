from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from .models import Article

# Create your views here.


def blog_list(request):
    # Get all published articles with publish_on later than now
    articles = Article.objects.filter(
        Q(publish_on__lte=datetime.now()) &
        Q(published=True)
    )

    context = {
        'articles': articles,
    }
    return render(request, 'blog/blog_list.html', context)
