"""Context processors for the shop application."""
from .cart import Cart


def cart_context(request):
    cart = Cart(request)
    return {
        'cart': cart,
        'cart_item_count': cart.get_item_count(),
        'cart_total': cart.get_total_price(),
    }
