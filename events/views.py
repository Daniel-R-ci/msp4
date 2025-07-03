from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

from .models import Event, Event_Registration

# Create your views here.


# Get all published events
def event_list(request):
    """
    Get all published events
    """

    # Get all published articles with publish_on later than now
    event_list = Event.objects.filter(
        Q(publish_on__lte=datetime.now()) &
        Q(published=True)
    ).order_by('time')

    # Use pagination, 12 posts per page
    paginator = Paginator(event_list, 12)
    page_number = request.GET.get('page', 1)
    events = paginator.page(page_number)

    context = {
        'events': events,

    }
    return render(request, 'events/event_list.html', context)


# Get a specific event
def event_detail(request, event_id):
    """
    Get specific article
    """

    event = get_object_or_404(
        Event,
        id=event_id,
        published=True
    )

    user_already_registered = False
    if request.user.is_authenticated:
        if Event_Registration.objects.filter(event=event, user=request.user).exists():
            user_already_registered = True

    # Used to get back to previous page, regardless of pagination
    # Code found at https://groups.google.com/g/django-users/c/wWvhbbXq1tA
    # Adjusted to suit purpose
    previous_url = request.META.get('HTTP_REFERER', '/events')

    context = {
        'event': event,
        'previous_url': previous_url,
        'user_already_registered': user_already_registered
    }

    return render(request, 'events/event_detail.html', context)
