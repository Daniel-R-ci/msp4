from django.shortcuts import render
from django.contrib import messages

from .forms import Contact_Form

# Create your views here.


# Render the about view with contact form
def about_view(request):
    """
    Render about view including contact form
    """

    # Check for posting of new contact form
    if request.method == "POST":
        contact_form = Contact_Form(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()
            messages.success(request,
                             "Thank you for contacting The Creative Barn!\nWe will get back to you as soon as possible.")
            contact_form = Contact_Form()
    else:
        contact_form = Contact_Form()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'about/about.html', context)
