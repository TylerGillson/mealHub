from django import forms
#from django.forms import widgets
from users.models import Profile, MealRequest
from meals.models import Meal
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets
import datetime

class MealRequestForm(forms.ModelForm):
    class Meta:
        model = MealRequest
        fields = ('mealRequestName', 'servings_requested', 'other')
        labels = {
            'mealRequestName': _('Meal Requested'),
            'servings_requested': _('Servings Requested')
        }
        help_texts = {
            'other': _("ex: I'm alergic to peanuts")
        }

class CreateMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('mealname', 'mealdesc', 'servings_available', 'photo')
        labels = {
            'mealdesc': _('Meal Description'),
        }
        widgets = {
            'date_available': widgets.AdminSplitDateTime(),
        }
