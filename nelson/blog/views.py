from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from base.forms import SubscribeForm
from .models import Blog, BlogBanner
from base.models import BlogDetailBanner
from cart.models import CartProduct, Cart
from django.core.paginator import Paginator


def blog(request):

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    blog_banner = BlogBanner.objects.all()
    subscribe = SubscribeForm()
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    # Set up Pagination
    p = Paginator(Blog.objects.all(), 1)
    page = request.GET.get('page')
    blog_posts = p.get_page(page)
    nums = 'a' * blog_posts.paginator.num_pages

    data = {
        'blog_banner': blog_banner,
        'subscribe_form': subscribe,
        'cart': cart,
        'blog_posts': blog_posts,
        'nums': nums,
    }

    return render(request, 'blog.html', context=data)


def blog_details(request, id, slug):
    post = get_object_or_404(Blog, id=id, slug=slug)
    blog_detail_banner = BlogDetailBanner.objects.all()
    subscribe = SubscribeForm()
    recent_posts = Blog.objects.all()[:4]
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    data = {
        'post': post,
        'cart': cart,
        'banner': blog_detail_banner,
        'subscribe_form': subscribe,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog-details.html', context=data)
