from django.http import HttpResponse


class Stripe_Web_Hook_Handler:
    """To Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle any generic or unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def on_payment_intent_succeeded(self, event):
        """
        Handle Stripe payment_intent.succeeded webhook if successful
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def on_payment_intent_payment_failed(self, event):
        """
        Handle Stripe payment_intent.payment_failed webhook if failed
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
