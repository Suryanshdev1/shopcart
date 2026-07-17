"""Session-based shopping cart implementation."""
from decimal import Decimal
from .models import CartItem, Product


class Cart:
    """Shopping cart class that wraps session and database storage."""

    def __init__(self, request):
        self.session = request.session
        self.session_key = request.session.session_key or request.session._get_or_create_session_key()
        self._items = None

    def __iter__(self):
        if self._items is None:
            self._items = list(
                CartItem.objects.filter(session_key=self.session_key).select_related('product', 'product__category')
            )
        for item in self._items:
            yield {
                'product': item.product,
                'quantity': item.quantity,
                'price': Decimal(str(item.product.price)),
                'total_price': item.total_price,
                'item': item,
            }

    def __len__(self):
        return sum(item.quantity for item in self._items or [])

    def add(self, product, quantity=1, update_quantity=False):
        if not product.in_stock:
            raise ValueError(f'{product.name} is out of stock.')
        if quantity > product.stock:
            raise ValueError(f'Only {product.stock} units of {product.name} available.')

        item, created = CartItem.objects.get_or_create(
            session_key=self.session_key,
            product=product,
            defaults={'quantity': 0}
        )

        if update_quantity:
            item.quantity = quantity
        else:
            new_quantity = item.quantity + quantity
            if new_quantity > product.stock:
                raise ValueError(f'Cannot add {quantity} more. Only {product.stock - item.quantity} available.')
            item.quantity = new_quantity

        item.save()
        self._items = None

    def remove(self, product):
        CartItem.objects.filter(session_key=self.session_key, product=product).delete()
        self._items = None

    def clear(self):
        CartItem.objects.filter(session_key=self.session_key).delete()
        self._items = None

    def get_total_price(self):
        total = Decimal('0.00')
        for item in self:
            total += Decimal(str(item['total_price']))
        return total

    def get_item_count(self):
        return len(self)

    def is_empty(self):
        return not CartItem.objects.filter(session_key=self.session_key).exists()
