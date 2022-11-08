from django import forms
from .models import Subscribe, WriteUs
from django.contrib.auth import get_user_model, authenticate


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


User = get_user_model()


class RegistrationUserForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ('username', 'password', )

    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'username',
        'value': '',
        'type': 'text',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password',
        'value': '',
        'type': 'password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password2',
        'value': '',
        'type': 'password',
    }))

    def clean_password2(self):
        data = self.cleaned_data

        if data['password'] == data['password2']:
            return data['password']
        raise forms.ValidationError('Паролі не співпадають!')


class LoginUserForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'username',
        'value': '',
        'type': 'text',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password',
        'value': '',
        'type': 'password',
    }))

    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Логін або пароль введені невірно!')
            return super().clean()

