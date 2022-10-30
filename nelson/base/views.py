from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Category, Product, ProductPhoto, Advantages, DiscountBanner, Furniture, HomeBanner, Review, Brands
from .models import Contact, Blog, BlogBanner, AboutBanner, About, Team, FaqBanner, Faq, ShopBanner, ContactBanner
from .forms import SubscribeForm, WriteUsForm
from cart.cart import Cart


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

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    new_arrivals = Product.objects.filter(new_arrival=True)
    img = ProductPhoto.objects.filter(position=1)
    shop_banner = ShopBanner.objects.all()
    subscribe = SubscribeForm()
    cart = Cart(request)

    data = {'categories': categories,
            'products': products,
            'new_arrivals': new_arrivals,
            'photo': img,
            'shop_banner': shop_banner,
            'subscribe_form': subscribe,
            }

    return render(request, 'shop.html', context=data)


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request,
                  'single-product.html',
                  {'product': product})


def about(request):

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    about_banner = AboutBanner.objects.all()
    about = About.objects.all()
    team = Team.objects.all()
    discount_banner = DiscountBanner.objects.all()
    advantages = Advantages.objects.all()
    review = Review.objects.all()
    subscribe = SubscribeForm()

    data = {
        'about_banner': about_banner,
        'about': about,
        'team': team,
        'discount_banner': discount_banner,
        'advantages': advantages,
        'review': review,
        'subscribe_form': subscribe,
    }

    return render(request, 'about.html', context=data)


def faq(request):

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    faq = Faq.objects.all()
    faq_banner = FaqBanner.objects.all()
    subscribe = SubscribeForm()

    data = {
        'faq': faq,
        'faq_banner': faq_banner,
        'subscribe_form': subscribe,
    }

    return render(request, 'faq.html', context=data)


def compare(request):
    return HttpResponse('Hello from compare page')


def cart(request):
    return HttpResponse('Hello from cart page')


def checkout(request):
    return HttpResponse('Hello from checkout page')


def wishlist(request):
    return HttpResponse('Hello from wishlist page')


def my_account(request):
    return render(request, 'my-account.html')


def login(request):
    return render(request, 'login-register.html')


def blog(request):

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    blog_post = Blog.objects.all()
    blog_banner = BlogBanner.objects.all()
    subscribe = SubscribeForm()

    data = {
        'blog_post': blog_post,
        'blog_banner': blog_banner,
        'subscribe_form': subscribe,
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
    contact_banner = ContactBanner.objects.all()

    data = {'write_us_from': write_us,
            'contact_banner': contact_banner,
            }
    return render(request, 'contact.html', context=data)
