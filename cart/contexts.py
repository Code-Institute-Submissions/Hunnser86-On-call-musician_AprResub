from decimal import Decimal
from django.conf import settings

def cart_contents(request):
    """ A context processor for the cart items"""
    cart_items = []
    total = 0
    service_count = 0
    discount = 0

    if total < settings.TEN_PERCENT_DISCOUNT:
        discount = total * Decimal(settings.SINGLE_PRODUCT_COUNT)
        discount_delta = settings.TEN_PERCENT_DISCOUNT - total
    else:
        discount = 0
        discount_delta = 0


    grand_total = discount + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'service_count': service_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'ten_percent_discount': settings.TEN_PERCENT_DISCOUNT,
        'grand_total': grand_total,

    }

    return context

