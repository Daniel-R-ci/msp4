from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from datetime import datetime

from .forms import UpdateNameForm
from events.models import Event_Registration
# Create your views here.


# List user information
def user_profile(request):
    """
    List user information
    """

    upcoming_events = Event_Registration.objects.filter(
        Q(event_time__gte=datetime.now()) &
        Q(user=request.user)
    ).order_by('event_time')

    previous_events = Event_Registration.objects.filter(
        Q(event_time__lte=datetime.now()) &
        Q(user=request.user)
    ).order_by('event_time')

    context = {
        'upcoming_events': upcoming_events,
        'previous_events': previous_events,
    }

    return render(request, 'user_profile/user_profile.html', context)


# Ask for full name first time a new user log in
def request_name(request):
    """
    Ask for full name first time a new user log in
    """

    if request.method == "POST":
        update_name_form = UpdateNameForm(data=request.POST)
        if update_name_form.is_valid():
            user = request.user
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            messages.success(request, "Thank you for completing the \
                             registration by providing your full name!")
            return redirect('home')
        else:
            messages.error(request, "There was a problem completing the \
                           registration. Please try again!")

    update_name_form = UpdateNameForm()

    context = {
        'update_name_form': update_name_form,
    }

    return render(request, 'user_profile/request_name.html', context)
