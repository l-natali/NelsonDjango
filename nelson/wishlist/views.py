from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from .wishlist import Wishlist
from base.models import Product
from cart.cart import Cart
from django.conf import settings


@require_GET
def wishlist_add(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wishlist.add(product=product)
    return redirect('shop:shop')


def wishlist_remove(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wishlist.remove(product)
    return redirect('wishlist:wishlist_detail')


def wishlist_detail(request):
    wishlist = Wishlist(request)
    return render(request, 'wishlist.html', {'wishlist': wishlist})
