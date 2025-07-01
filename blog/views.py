from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

from .models import Article

# Create your views here.


# Get all published articles
def blog_list(request):
    """
    Get all published articles
    """

    # Get all published articles with publish_on later than now
    article_list = Article.objects.filter(
        Q(publish_on__lte=datetime.now()) &
        Q(published=True)
    )

    # Use pagination, 12 posts per page
    paginator = Paginator(article_list, 12)
    page_number = request.GET.get('page', 1)
    articles = paginator.page(page_number)

    context = {
        'articles': articles,
    }
    return render(request, 'blog/blog_list.html', context)


# Get a specific article
def blog_detail(request, article_id):
    """
    Get specific article
    """

    article = get_object_or_404(
        Article,
        id=article_id,
        published=True
    )

    # Used to get back to previous page, regardless of pagination
    # Code found at https://groups.google.com/g/django-users/c/wWvhbbXq1tA
    # Adjusted to suit purpose
    previous_url = request.META.get('HTTP_REFERER', '/blog')

    context = {
        'article': article,
        'previous_url': previous_url
    }

    return render(request, 'blog/blog_post.html', context)
