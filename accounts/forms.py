from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Enter a valid email address')

    error_messages = {
        'password_too_short': _('Password must be at least 8 characters long.'),
        'password_mismatch': _('Passwords do not match.'),
    }
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'password1': _('Password'),
            'password2': _('Confirm Password'),
        }
        help_texts = {
            'password1': _('Password must be at least 8 characters long.'),
        }


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError(_('Password must be at least 8 characters long.'), code='password_too_short')
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Passwords do not match.'), code='password_mismatch')
        return password2

class SignInForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ('username', 'password')



