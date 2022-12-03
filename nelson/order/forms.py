from django import forms
from django.shortcuts import redirect

from .models import Order
from cart.models import Cart


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'email', 'phone', 'country', 'city', 'state', 'zip_code', ]
