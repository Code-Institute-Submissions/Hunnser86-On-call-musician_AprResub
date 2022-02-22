from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from services.models import Service

def view_cart(request):
    """ A view to render the cart page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified service to the cart """

    service = get_object_or_404(Service, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    messages.success(request, f'Added {service.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)





def remove_from_cart(request, item_id):
    """ Remove items from the cart """
    try:
        service = get_object_or_404(Service, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request,
                         f'Removed {service.name} from your cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
