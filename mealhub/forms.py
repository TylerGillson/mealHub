from django import forms
from users.models import Profile
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               help_text='Passwords must be at least 8 digits.')
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': _(''),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'zip_code')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'zip_code')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
