"""Views for the shop application."""
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Category, Product, CartItem
from .forms import CartAddForm, ContactForm
from .cart import Cart


def home(request):
    featured_products = Product.objects.filter(featured=True, available=True)[:8]
    categories = Category.objects.filter(is_active=True)[:6]
    new_arrivals = Product.objects.filter(available=True).order_by('-created_at')[:4]
    return render(request, 'shop/home.html', {
        'featured_products': featured_products,
        'categories': categories,
        'new_arrivals': new_arrivals,
    })


def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_active=True)
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    sort = request.GET.get('sort', 'newest')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created_at')
    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'shop/product_list.html', {
        'products': page_obj,
        'categories': categories,
        'query': query,
        'current_category': category_slug,
        'current_sort': sort,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'related_products': related_products,
        'cart_add_form': CartAddForm(),
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, available=True)
    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'shop/category_detail.html', {
        'category': category,
        'products': page_obj,
    })


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, available=True)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        try:
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
            messages.success(request, f'{product.name} added to your cart.')
        except ValueError as e:
            messages.error(request, str(e))
    else:
        messages.error(request, 'Invalid quantity.')
    return redirect('shop:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f'{product.name} removed from your cart.')
    return redirect('shop:cart_detail')


@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = request.POST.get('quantity', 1)
    try:
        quantity = int(quantity)
        if 1 <= quantity <= 99:
            cart.add(product=product, quantity=quantity, update_quantity=True)
            messages.success(request, 'Cart updated successfully.')
        else:
            messages.error(request, 'Quantity must be between 1 and 99.')
    except ValueError:
        messages.error(request, 'Invalid quantity.')
    return redirect('shop:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_form'] = CartAddForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'shop/cart.html', {'cart': cart})


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('shop:contact')
    else:
        form = ContactForm()
    return render(request, 'shop/contact.html', {'form': form})
