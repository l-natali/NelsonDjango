from django import forms
from .models import Subscribe, WriteUs


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


class WriteUsForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'contact-form-style mb-20',
            'name': 'name',
            'placeholder': '',
            'type': 'text',
        })
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'contact-form-style mb-20',
            'name': 'email',
            'placeholder': '',
            'type': 'email',
        })
    )

    notabot = forms.ModelChoiceField(
        queryset=WriteUs.objects.filter(notabot=True),
        widget=forms.CheckboxInput(attrs={
            'class': 'check-box',
            'type': 'checkbox',
            'id': 'create_account',
        })
    )

    message = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'class': 'pl-15',
            'name': 'message',
            'placeholder': 'Type your message here..'
        })
    )

    class Meta:
        model = WriteUs
        fields = ('name', 'email', 'notabot', 'message', )
