from django.shortcuts import render


def view_cart(request):
    """ A view to render the cart page"""

    return render(request, 'cart/cart.html')