from django import forms
from .models import Customer
from django.contrib.auth.models import User


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_username(self):
        uname = self.cleaned_data.get('username')
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Користувач з таким ім'ям вже існує!")
        return uname


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)