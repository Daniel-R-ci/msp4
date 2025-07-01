from django.shortcuts import render


# Create your views here.
def event_list(request):

    context = {
        'test_value': True
    }
    return render(request, 'events/events.html', context)
