from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Product, ProductPhoto, Advantages, DiscountBanner, Furniture, HomeBanner, Review, Brands
from .models import Contact, Blog, BlogBanner, AboutBanner, About, Team
from .forms import SubscribeForm, WriteUsForm

# menu = [{'title': 'Shop', 'url_name': 'shop'},
#
#         ]


def base(request):
    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    new_arrivals = Product.objects.filter(new_arrival=True)
    advantages = Advantages.objects.all()
    discount_banner = DiscountBanner.objects.all()
    furniture = Furniture.objects.all()
    home_banner = HomeBanner.objects.all()
    product_photo = ProductPhoto.objects.all()
    review = Review.objects.all()
    brands = Brands.objects.all()
    contact = Contact.objects.all()
    subscribe = SubscribeForm()
    blog = Blog.objects.all()[:3]

    data = {'categories': categories,
            'products': products,
            'new_arrivals': new_arrivals,
            'advantages': advantages,
            'discount_banner': discount_banner,
            'furniture': furniture,
            'home_banner': home_banner,
            'product_photo': product_photo,
            'review': review,
            'brands': brands,
            'contact': contact,
            'subscribe_form': subscribe,
            'blog': blog,
            }

    return render(request, 'index.html', context=data)


def shop(request):
    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    new_arrivals = Product.objects.filter(new_arrival=True)
    img = ProductPhoto.objects.filter(position=1)

    data = {'categories': categories,
            'products': products,
            'new_arrivals': new_arrivals,
            'photo': img, }

    return render(request, 'shop.html', context=data)


def about(request):

    about_banner = AboutBanner.objects.all()
    about = About.objects.all()
    team = Team.objects.all()
    discount_banner = DiscountBanner.objects.all()
    advantages = Advantages.objects.all()
    review = Review.objects.all()

    data = {
        'about_banner': about_banner,
        'about': about,
        'team': team,
        'discount_banner': discount_banner,
        'advantages': advantages,
        'review': review,
    }

    return render(request, 'about.html', context=data)


def faq(request):
    return HttpResponse('Hello from faq page')


def compare(request):
    return HttpResponse('Hello from compare page')


def product_details(request):
    return HttpResponse('Hello from product_details page')


def cart(request):
    return HttpResponse('Hello from cart page')


def checkout(request):
    return HttpResponse('Hello from checkout page')


def wishlist(request):
    return HttpResponse('Hello from wishlist page')


def my_account(request):
    return HttpResponse('Hello from my-account page')


def login(request):
    return HttpResponse('Hello from login-register page')


def blog(request):

    blog_post = Blog.objects.all()
    blog_banner = BlogBanner.objects.all()

    data = {
        'blog_post': blog_post,
        'blog_banner': blog_banner
    }

    return render(request, 'blog.html', context=data)


def blog_details(request):
    return HttpResponse('Hello from blog-details page')


def contact(request):

    if request.method == 'POST':
        write_us = WriteUsForm(request.POST)
        if write_us.is_valid():
            write_us.save()
            return redirect('/')

    write_us = WriteUsForm()

    data = {'write_us_from': write_us,

    }
    return render(request, 'contact.html', context=data)
