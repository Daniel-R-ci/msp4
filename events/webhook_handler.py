from django.http import HttpResponse
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
        user_id = intent.metadata.user_id # noqa not currently used but would be needed to retrieve user and send email down below in TODO-comment 

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

            # TODO: Send an email to user informing that a reservation can't
            # be made but that the money will be refunded

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
