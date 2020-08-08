from django.shortcuts import render


def view_bag(request):
    """ A view that renderst the contents of the shopping bag page """

    return render(request, 'bag/bag.html')
