from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NEWACCOUNT

TYPE_CHOICES = (
    ('STUDENT', 'STUDENT'),
    ('BUSINESS', 'BUSINESS'),
    ('TOURIST', 'TOURIST'),

)
class CreateAccount(forms.Form):
    USERNAME = forms.CharField(max_length=400, label='Username')
    FIRSTNAME = forms.CharField(max_length=200,label='First Name')
    LASTNAME = forms.CharField(max_length=200, label='Last Name')
    EMAIL = forms.EmailField(label="Email")
    PASSWORD = forms.CharField(widget=forms.PasswordInput)
    REPASSWORD = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    ADDRESS = forms.CharField(max_length=200, label='Address')
    TYPE = forms.ChoiceField(choices=TYPE_CHOICES,label='TYpe')


    class Meta:
            model = NEWACCOUNT
            fields = ('USERNAME', 'FIRSTNAME', 'LASTNAME', 'EMAIL', 'PASSWORD', 'REPASSWORD', 'ADDRESS', 'TYPE')
