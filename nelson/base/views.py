from django.shortcuts import render, HttpResponse
from .models import Category, Product, ProductPhoto, Advantages, DiscountBanner, Furniture, HomeBanner, Review, Brands
from .models import Contact

menu = [{'title': 'Shop', 'url_name': 'shop'},

        ]


def base(request):
    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    new_arrivals = Product.objects.filter(new_arrival=True)
    advantages = Advantages.objects.all()
    discount_banner = DiscountBanner.objects.all()
    furniture = Furniture.objects.all()
    home_banner = HomeBanner.objects.all()
    product_photo = ProductPhoto.objects.filter(position=1)
    review = Review.objects.all()
    brands = Brands.objects.all()
    contact = Contact.objects.all()

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
            'contact': contact, }

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
