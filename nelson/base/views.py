from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Category, Product, ProductPhoto, Advantages, DiscountBanner, Furniture, HomeBanner, Review, Brands
from .models import Contact, AboutBanner, About, Team, FaqBanner, Faq, ShopBanner, ContactBanner
from .forms import SubscribeForm, WriteUsForm, RegistrationUserForm, LoginUserForm
from cart.cart import Cart
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Blog
from django.contrib.auth.decorators import login_required


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
    cart = Cart(request)

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
            'cart': cart,
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
    img = Product.objects.all()
    shop_banner = ShopBanner.objects.all()
    subscribe = SubscribeForm()
    cart = Cart(request)

    data = {'categories': categories,
            'products': products,
            'new_arrivals': new_arrivals,
            'photo': img,
            'shop_banner': shop_banner,
            'subscribe_form': subscribe,
            'cart': cart,
            }

    return render(request, 'shop.html', context=data)


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_visible=True)
    cart = Cart(request)
    print(product.photo)

    return render(request,
                  'single-product.html',
                  {'product': product,
                   'cart': cart,
                   })


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
    cart = Cart(request)

    data = {
        'about_banner': about_banner,
        'about': about,
        'team': team,
        'discount_banner': discount_banner,
        'advantages': advantages,
        'review': review,
        'subscribe_form': subscribe,
        'cart': cart,
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
    cart = Cart(request)

    data = {
        'faq': faq,
        'faq_banner': faq_banner,
        'subscribe_form': subscribe,
        'cart': cart,
    }

    return render(request, 'faq.html', context=data)


def compare(request):
    return HttpResponse('Hello from compare page')


def checkout(request):
    return HttpResponse('Hello from checkout page')


def my_account(request):

    cart = Cart(request)

    data = {'cart': cart,
            }

    return render(request, 'my-account.html', context=data)


def login_view(request):

    reg_form = RegistrationUserForm()
    login_form = LoginUserForm()
    cart = Cart(request)

    data = {'cart': cart,
            'reg_form': reg_form,
            'login_form': login_form,
            }

    reg_form = RegistrationUserForm(request.POST or None)
    login_form = LoginUserForm(request.POST or None)

    if login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/my-account')

    if reg_form.is_valid():
        new_user = reg_form.save(commit=False)
        new_user.set_password(reg_form.cleaned_data['password'])
        new_user.save()
        messages.success(request, 'success')
        return render(request, 'login-register.html', context=data)

    return render(request, 'login-register.html', context=data)


def logout_view(request):
    logout(request)
    return redirect('/')




def contact(request):

    if request.method == 'POST':
        if 'write_us' in request.POST:
            write_us = WriteUsForm(request.POST)
            if write_us.is_valid():
                write_us.save()
                return redirect('/')
        if 'subscribe_form' in request.POST:
            subscribe = SubscribeForm(request.POST)
            if subscribe.is_valid():
                subscribe.save()
                return redirect('/')

    write_us = WriteUsForm()
    contact_banner = ContactBanner.objects.all()
    subscribe = SubscribeForm()
    cart = Cart(request)

    data = {'write_us_from': write_us,
            'contact_banner': contact_banner,
            'subscribe_form': subscribe,
            'cart': cart,
            }
    return render(request, 'contact.html', context=data)
