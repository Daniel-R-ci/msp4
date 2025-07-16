from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator
from os import environ
from datetime import datetime
import stripe

from .models import Event, Event_Registration
from .forms import PaymentForm

# Create your views here.


# Get all published events
def event_list(request):
    """
    Get all published events
    """

    # Get all upcoming published events with publish_on later than now
    event_list = Event.objects.filter(
        Q(publish_on__lte=datetime.now()) &
        Q(time__gte=datetime.now()) &
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
    # Needed to make user_already_registered work
    # Remove all uncofirmed registrations older than five minutes
    Event_Registration.remove_unconfirmed_registrations()
    # Delete any previous uncompleted registration from current user
    Event_Registration.objects.filter(
        event=event, user=request.user, confirmed=False).delete()

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

        payment_form = PaymentForm(data=request.POST)

        if payment_form.is_valid():
            registration.confirmed = True
            registration.save()

            return redirect('event_confirmed', event_id=event_id)
        else:
            context = {
                'event': event,
                'payment_form': payment_form
            }
            return render(request, 'events/event_registration.html', context)

    else:
        if Event_Registration.objects.filter(event=event, user=request.user, confirmed=True).exists():
            raise Http404("You already have a confirmed reservation for this event")
        # Check that there are still available spots
        if event.available_spots < 1:
            raise Http404("No available spots")

        # Delete any previous uncompleted registration
        Event_Registration.objects.filter(
            event=event, user=request.user, confirmed=False).delete()

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
            payment_form = PaymentForm()

            # Stripe checkout session data
            stripe.api_key = environ.get('CLIENT_SECRET')
            intent = stripe.PaymentIntent.create(
                amount=int(round(event.cost * 100)),
                currency='gbp',
                metadata={'integration_check': 'accept_a_payment'},
            )

            context = {
                'event': event,
                'payment_form': payment_form,
                'stripe_public_key': environ.get('STRIPE_PUBLIC_KEY'),
                'client_secret': intent.client_secret,
            }
            return render(request, 'events/event_registration.html', context)


# Cancel an event registration
def cancel_event_registration(request, event_id):
    event = get_object_or_404(
        Event,
        id=event_id,
        published=True
    )
    # Delete any previous uncompleted registration
    Event_Registration.objects.filter(
        event=event, user=request.user, confirmed=False).delete()

    # Redirect user to event page
    return redirect('event_detail', event_id=event_id)


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

    messages.success(request, f"You have successfully registered for \
                     {registration.event_title}!")

    context = {
        'event': event,
        'registration': registration,
    }

    return render(request, 'events/event_confirmed.html', context)
