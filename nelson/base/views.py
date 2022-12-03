from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db.models import Q
from .models import Category, Product, ProductPhoto, Advantages, DiscountBanner, Furniture, HomeBanner, Review, Brands
from .models import Contact, AboutBanner, About, Team, FaqBanner, Faq, ShopBanner, ContactBanner, Profile
from .models import ProductDetailBanner, AccountBanner, LoginBanner
from .forms import SubscribeForm, WriteUsForm, ProfileForm, PasswordChangingForm
from cart.models import CartProduct, Cart
from compare.compare import Compare
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView
from order.views import NelsonMixin


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
    product_photo = ProductPhoto.objects.filter(position=1)
    review = Review.objects.all()
    brands = Brands.objects.all()
    contact = Contact.objects.all()
    subscribe = SubscribeForm()
    blog = Blog.objects.all()[:3]
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

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
    img = Product.objects.filter(id=1)
    shop_banner = ShopBanner.objects.all()
    subscribe = SubscribeForm()
    compare = Compare(request)
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    # Set up Pagination
    p = Paginator(Product.objects.filter(is_visible=True), 1)
    page = request.GET.get('page')
    product_list = p.get_page(page)
    nums = 'a' * product_list.paginator.num_pages

    data = {'categories': categories,
            'products': products,
            'new_arrivals': new_arrivals,
            'photo': img,
            'shop_banner': shop_banner,
            'subscribe_form': subscribe,
            'cart': cart,
            'compare': compare,
            'product_list': product_list,
            'nums': nums,
            }

    return render(request, 'shop.html', context=data)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, is_visible=True)
    product_detail_banner = ProductDetailBanner.objects.all()
    subscribe = SubscribeForm()
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    return render(request,
                  'single-product.html',
                  {'product': product,
                   'cart': cart,
                   'banner': product_detail_banner,
                   'subscribe_form': subscribe,
                   })


class AboutView(NelsonMixin, View):

    def get(self, request):
        about_banner = AboutBanner.objects.all()
        about = About.objects.all()
        team = Team.objects.all()
        discount_banner = DiscountBanner.objects.all()
        advantages = Advantages.objects.all()
        review = Review.objects.all()
        subscribe = SubscribeForm()
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

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

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

# def about(request):
#
#     if request.method == 'POST':
#         subscribe = SubscribeForm(request.POST)
#         if subscribe.is_valid():
#             subscribe.save()
#             return redirect('/')
#
#     about_banner = AboutBanner.objects.all()
#     about = About.objects.all()
#     team = Team.objects.all()
#     discount_banner = DiscountBanner.objects.all()
#     advantages = Advantages.objects.all()
#     review = Review.objects.all()
#     subscribe = SubscribeForm()
#     # cart = Cart(request)
#
#     data = {
#         'about_banner': about_banner,
#         'about': about,
#         'team': team,
#         'discount_banner': discount_banner,
#         'advantages': advantages,
#         'review': review,
#         'subscribe_form': subscribe,
#         # 'cart': cart,
#     }
#
#     return render(request, 'about.html', context=data)


def faq(request):

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    faq = Faq.objects.all()
    faq_banner = FaqBanner.objects.all()
    subscribe = SubscribeForm()
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    data = {
        'faq': faq,
        'faq_banner': faq_banner,
        'subscribe_form': subscribe,
        'cart': cart,
    }

    return render(request, 'faq.html', context=data)


# @login_required(login_url='login.html')
# def my_account(request):
#
#     profile_form = ProfileForm()
#     profile = Profile.objects.all()
#     account_banner = AccountBanner.objects.all()
#     subscribe = SubscribeForm()
#     cart_id = request.session.get('cart_id', None)
#     if cart_id:
#         cart = Cart.objects.get(id=cart_id)
#     else:
#         cart = None
#
#     data = {'profile_form': profile_form,
#             'profile': profile,
#             'banner': account_banner,
#             'subscribe_form': subscribe,
#             'cart': cart,
#             }
#
#     if request.method == 'POST':
#         profile = ProfileForm(request.POST, instance=request.user.profile)
#         if profile.is_valid():
#             profile.save()
#             return redirect('/my-account')
#
#     return render(request, 'my-account.html', context=data)



# def login_view(request):
#
#     reg_form = RegistrationUserForm()
#     login_form = LoginUserForm()
#     login_banner = LoginBanner.objects.all()
#     subscribe = SubscribeForm()
#     cart_id = request.session.get('cart_id', None)
#     if cart_id:
#         cart = Cart.objects.get(id=cart_id)
#     else:
#         cart = None
#
#     data = {'reg_form': reg_form,
#             'login_form': login_form,
#             'banner': login_banner,
#             'subscribe_form': subscribe,
#             'cart': cart,
#             }
#
#     reg_form = RegistrationUserForm(request.POST or None)
#     login_form = LoginUserForm(request.POST or None)
#
#     if login_form.is_valid():
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/my-account')
#
#     if reg_form.is_valid():
#         new_user = reg_form.save(commit=False)
#         new_user.set_password(reg_form.cleaned_data['password'])
#         new_user.save()
#         login(request, new_user)
#         messages.success(request, 'success')
#         return redirect('/my-account')
#
#     return render(request, 'login.html', context=data)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('/')

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
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    data = {'write_us_from': write_us,
            'contact_banner': contact_banner,
            'subscribe_form': subscribe,
            'cart': cart,
            }
    return render(request, 'contact.html', context=data)


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        result = Product.objects.filter(Q(title__icontains=kw) | Q(description__icontains=kw))
        context['result'] = result
        return context
