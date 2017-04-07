from django import forms
from .models import Profile, Meal, MealRequest
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets
import datetime

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               help_text='Passwords must be at least 8 digits.')
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        labels = {
            'first_name': _('First Name'),
            'email': _('Email Address')
        }
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
        labels = {
            'first_name': _('First Name'),
            'email': _('Email Address')
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'address', 'city', 'state', 'zip_code')
        labels = {
            'user_type': _('User Type'),
            'zip_code': _('Zip Code')
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'address', 'city', 'state', 'zip_code')
        labels = {
            'user_type': _('User Type'),
            'zip_code': _('Zip Code')
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class MealRequestForm(forms.ModelForm):
    class Meta:
        model = MealRequest
        fields = ('mealRequestName', 'servings_requested', 'other')
        labels = {
            'mealRequestName': _('Meal Requested'),
            'servings_requested': _('Servings Requested')
        }
        help_texts = {
            'other': _("ex: I'm allergic to peanuts.")
        }

class CreateMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('mealname', 'mealdesc', 'servings_available', 'ingredients', 'photo')
        labels = {
            'mealname': _('Meal Name'),
            'mealdesc': _('Meal Description'),
            'servings_available': _('Servings Available'),
        }
