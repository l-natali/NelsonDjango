from django.shortcuts import render, HttpResponse
from .models import Category, Product, ProductPhoto

menu = [{'title': 'Shop', 'url_name': 'shop'},

        ]


def base(request):
    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    new_arrivals = Product.objects.filter(new_arrival=True)

    data = {'categories': categories,
            'products': products,
            'new_arrivals': new_arrivals, }

    return render(request, 'index.html', context=data)


def shop(request):
    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    new_arrivals = Product.objects.filter(new_arrival=True)
    img = ProductPhoto.objects.all()

    data = {'categories': categories,
            'products': products,
            'new_arrivals': new_arrivals,
            'photo': img, }

    return render(request, 'shop.html', context=data)


def about(request):
    return render(request, 'about.html')


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
    return HttpResponse('Hello from blog page')


def blog_details(request):
    return HttpResponse('Hello from blog-details page')


def contact(request):
    return HttpResponse('Hello from contact page')
