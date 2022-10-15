from django import forms
from .models import Subscribe


class SubscribeForm(forms.ModelForm):

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'placeholder': 'Enter Your Email Address Here...'

        })
    )

    class Meta:
        model = Subscribe
        fields = ('email', )