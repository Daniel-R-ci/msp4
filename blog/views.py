from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator

from .models import Article, Article_Comment
from .forms import Article_Comment_Form

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
    ).order_by('-publish_on')

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

    comments = Article_Comment.objects.filter(
        article=article).order_by('-posted_on')

    if request.method == "POST":
        comment_form = Article_Comment_Form(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment saved successfully!")
        else:
            messages.error(request, "An error occured posting your comment.\
                            Please try again!")

    # Used to get back to previous page, regardless of pagination
    # Code found at https://groups.google.com/g/django-users/c/wWvhbbXq1tA
    # Adjusted to suit purpose
    previous_url = request.META.get('HTTP_REFERER', '/blog')

    comment_form = Article_Comment_Form()

    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'previous_url': previous_url
    }

    return render(request, 'blog/blog_post.html', context)


# Edit and update a comment
def edit_comment(request, article_id, comment_id):
    """
    Edit and update an article comment
    """

    if request.method == "POST":
        comment = get_object_or_404(
            Article_Comment,
            id=comment_id,
            user=request.user
        )

        comment_form = Article_Comment_Form(request.POST, request.FILES)

        if comment_form.is_valid():
            comment.comment = comment_form.cleaned_data['comment']
            image = comment_form.cleaned_data['image']
            if image:
                comment.image = image
            else:
                comment.image = None
            comment.save()

    return redirect('blog_post', article_id=article_id)


# Delete a comment
def delete_comment(request, article_id, comment_id):
    """
    Delete an article comment
    """
    Article_Comment.objects.filter(pk=comment_id).delete()
    return redirect('blog_post', article_id=article_id)
