from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

from .models import Article

# Create your views here.


def blog_list(request):
    # Get all published articles with publish_on later than now
    article_list = Article.objects.filter(
        Q(publish_on__lte=datetime.now()) &
        Q(published=True)
    )

    paginator = Paginator(article_list, 12)
    page_number = request.GET.get('page', 1)
    articles = paginator.page(page_number)

    context = {
        'articles': articles,
    }
    return render(request, 'blog/blog_list.html', context)
