from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Enter your full name')

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Enter your full name')
    type = forms.ChoiceField(required=False, help_text='Enter your type')

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2', 'type',)