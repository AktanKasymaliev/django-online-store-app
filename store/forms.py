from django.contrib.auth.forms import AuthenticationForm
from c_user.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'example@example.com',
    # }))
    # password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Пароль',
    # }))
    class Meta:
        model = User
        fields = ('email', 'password')


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email')
