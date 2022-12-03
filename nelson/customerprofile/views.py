from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, FormView
from .forms import CustomerRegistrationForm, CustomerLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from order.views import NelsonMixin
from order.models import Order
from base.forms import SubscribeForm
from cart.models import CartProduct, Cart
from .models import Customer


class CustomerRegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('my-account')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            return next_url
        else:
             return self.success_url


class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class CustomerLoginView(FormView):
    template_name = 'login.html'
    form_class = CustomerLoginForm
    success_url = reverse_lazy('my-account')

    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data.get('password')
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'Логін або пароль не співпадають!'})

        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            return next_url
        else:
             return self.success_url


class CustomerProfileView(NelsonMixin, TemplateView):
    template_name = 'my-account.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/profile/login/?next=/profile/')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        orders = Order.objects.filter(cart__customer=customer)
        context['orders'] = orders
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart

        return context
