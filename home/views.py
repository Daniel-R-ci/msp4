from django.shortcuts import render
from django.db.models import Q
from datetime import datetime

from blog.models import Article
from events.models import Event

# Create your views here.


# Get all data needed for index view
def home_view(request):
    """
    Get all data needed for index view
    """

    # Object slicing example found at
    # https://stackoverflow.com/questions/5234090/how-to-take-the-first-n-items-from-a-generator-or-list

    articles = Article.objects.filter(
        Q(publish_on__lte=datetime.now()) &
        Q(published=True)
    ).order_by('-publish_on')[:3]

    events = Event.objects.filter(
        Q(publish_on__lte=datetime.now()) &
        Q(time__gte=datetime.now()) &
        Q(published=True)
    ).order_by('time')[:3]

    context = {
        'articles': articles,
        'events': events,
    }

    return render(request, 'home/index.html', context)
