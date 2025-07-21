from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import stripe
import time

from .models import Event_Registration


# Handle Stripe webhooks
class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook from Stripe
        """

        # Sleep for 10 seconds before continuing, to make time for database
        # and server to complete work
        time.sleep(10)

        intent = event.data.object
        pid = intent.id
        registration_id = intent.metadata.registration_id
        user_id = intent.metadata.user_id

        # Check if the order has been payed
        if Event_Registration.objects.filter(pk=registration_id).exists():
            # This triggers if registration is successfull,
            # or if preliminary booking still exists

            registration = Event_Registration.objects.get(pk=registration_id)

            if registration.confirmed is False:
                # Payment has not been confirmed
                # Set confirmed to true and save
                registration.confirmed = True
                registration.save()

        else:
            # This triggers if there no longer is a preliminary reservation
            # Instead of creating a new order, refund the customer
            intent = stripe.PaymentIntent.retrieve(pid, expand=['charges'])
            payment_intent_id = intent['id']
            charges = stripe.Charge.list(payment_intent=payment_intent_id)
            charge_id = charges['data'][0]['id']

            stripe.Refund.create(
                charge=charge_id,
                reason='requested_by_customer',
                metadata={'note': 'Customer refunded: Reservation \
                          not completed'},
            )

            # Send an email to user informing that a reservation can't
            # be made but that the money will be refunded
            user = User.objects.get(pk=user_id)
            send_mail(
                subject='[The Creative Barn] - An error occured \
                    during registration',
                message=(
                    f'Hello {user.first_name} {user.last_name}. We are very '
                    'sorry but an error occured while you where trying to '
                    'register for an event with us.\n\n'
                    'Although a reservation could not be made, we have told '
                    'our bank to immediately refund the money that was '
                    'incorrectly deducted from your accout during the failed '
                    'registration attempt.\n\n'
                    'We offer our sincere apologies, and do not hesitate to '
                    'contact us if there are any further problems.\n\n'
                    'Best regards, Arthur and Trillian!'),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
