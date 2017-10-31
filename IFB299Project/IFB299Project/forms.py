from django import forms

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
    TYPE = forms.ChoiceField(choices=TYPE_CHOICES,label='Type')

    class Meta:
        model = NEWACCOUNT
        fields = ('USERNAME', 'FIRSTNAME', 'LASTNAME', 'EMAIL', 'PASSWORD', 'REPASSWORD', 'ADDRESS', 'TYPE')


# Login form to create the input fields for general account login
class LoginForm(forms.Form):
    USERNAME = forms.CharField(max_length=400, label='Username')
    PASSWORD = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = NEWACCOUNT
        labels = {
        'USERNAME': "Username",
        "EMAIL": "Email Account",
        }
        fields = ['USERNAME', 'PASSWORD']

    # Overriding the generic unique validation function for the ACCOUNTNO field
    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        try:
            self.instance.validate_unique(exclude=exclude)
        except forms.ValidationError as e:
            try:
                del e.error_dict['EMAIL'] #if ACCOUNTNO unique validation occurs it will be omitted and form.is_valid() method pass
            except:
                pass                          # if any other error occours
            self._update_errors(e)