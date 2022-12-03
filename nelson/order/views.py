from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm
from cart.models import Cart, CartProduct
from django.views.generic import TemplateView, View, CreateView
from customerprofile.models import Customer


class NelsonMixin(object):
    def dispatch(self, request, *args, **kwargs):
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            if request.user.is_authenticated and request.user.customer:
                cart_obj.customer = request.user.customer
                cart_obj.save()
        return super().dispatch(request, *args, **kwargs)


class CheckoutView(NelsonMixin, CreateView):

    login_url = 'customerprofile/login'
    redirect_field_name = 'redirect_to'
    template_name = 'checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
            return redirect('/profile/login/?next=/order/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context['cart'] = cart_obj
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.total = cart_obj.total
            form.instance.status = 'created'
            del self.request.session['cart_id']
        else:
            return redirect('home')

        return super().form_valid(form)
