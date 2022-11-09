from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from base.forms import SubscribeForm
from .models import Blog, BlogBanner
from cart.cart import Cart


def blog(request):

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    blog_post = Blog.objects.all()
    blog_banner = BlogBanner.objects.all()
    subscribe = SubscribeForm()
    cart = Cart(request)

    data = {
        'blog_post': blog_post,
        'blog_banner': blog_banner,
        'subscribe_form': subscribe,
        'cart': cart,
    }

    return render(request, 'blog.html', context=data)


def blog_details(request, id, slug):
    post = get_object_or_404(Blog, id=id, slug=slug)
    cart = Cart(request)

    data = {
        'post': post,
        'cart': cart,
    }
    return render(request, 'blog-details.html', context=data)
