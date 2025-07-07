from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.http import Http404
from datetime import datetime
from django.core.paginator import Paginator

from .models import Event, Event_Registration
from .forms import TempPaymentForm

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
    Get specific event
    """

    event = get_object_or_404(
        Event,
        id=event_id,
        published=True
    )
    # Needed to make user_already_registered function
    Event_Registration.remove_unconfirmed_registrations()
    
    user_already_registered = False
    if request.user.is_authenticated:
        user_already_registered = Event_Registration.objects.filter(
            event=event, user=request.user).exists()

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


# Register for an event
def event_registration(request, event_id):
    """
    Register for an event
    """

    # Make sure user is logged in
    if not request.user.is_authenticated:
        raise Http404()

    # Delete unconfirmed reservations older than five minutes
    Event_Registration.remove_unconfirmed_registrations()

    event = get_object_or_404(
        Event,
        id=event_id,
        published=True
    )

    if request.method == "POST":
        registration = get_object_or_404(
            Event_Registration,
            event=event_id,
            user=request.user.id
        )

        temp_payment_form = TempPaymentForm(data=request.POST)

        if temp_payment_form.is_valid():
            registration.confirmed = True
            registration.save()
            return redirect('event_confirmed', event_id=event_id)
        else:
            context = {
                'event': event,
                'temp_payment_form': temp_payment_form
            }
            return render(request, 'events/event_registration.html', context)

    else:
        # Check that there are still available spots
        if event.available_spots < 1:
            raise Http404("No available spots")

        # Create new registration
        registration = Event_Registration()
        registration.event = event
        registration.user = request.user
        registration.event_title = event.title
        registration.event_time = event.time
        registration.event_cost = event.cost

        if event.cost == 0:
            # Event is free. Confirm reservation and send to event_confirmed
            registration.confirmed = True
            registration.save()
            return redirect('event_confirmed', event_id=event_id)
        else:
            registration.save()
            temp_payment_form = TempPaymentForm()

            context = {
                'event': event,
                'temp_payment_form': temp_payment_form
            }
            return render(request, 'events/event_registration.html', context)


# Show confirmation of event registration
def event_confirmed(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id,
        published=True
    )

    registration = get_object_or_404(
        Event_Registration,
        event=event,
        user=request.user)

    context = {
        'event': event,
        'registration': registration,
    }

    return render(request, 'events/event_confirmed.html', context)
