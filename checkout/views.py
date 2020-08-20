from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from shopping_bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oops, your bag is empty!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HHvadFYZsvd0wEhJLys62PoMMnLjWRrHfC9ABb8mvrjW3jlsCpkvKYzPcyvjYEfAxKJoJEPgSViI9wJ2gbxxjpE002qUtlFP6',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
