from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import MealRequest, User, Meal

# Create your views here.
class  LoginView(generic.ListView):
    template_name = 'users/login.html'

def ChefsView(request):
    mealrequest = MealRequest.objects.order_by('-date_requested')
    meal = Meal.objects.order_by('meal_rating')
    context = {'mealrequests': mealrequest, 'meal': meal,}
    return render(request, 'users/chef.html', context)


def MouthsView(request):
    meal = Meal.objects.order_by('-date_available')
    context = {'meal': meal,}
    return render(request, 'users/mouth.html', context)

def RegisterView(request):
    mealrequest = MealRequest.objects.order_by('-date_requested')
    meal = Meal.objects.order_by('meal_rating')
    context = {'mealrequests': mealrequest, 'meal': meal,}
    return render(request, 'users/register.html', context)

''' Date formatting example '''
#{% if meal %}
#{% for m in meal %}
#<tr>
#<td class="odd verticalLine">{{ m.user.username }}</td>
#<td class="odd verticalLine">{{ m.mealname }}</td>
#<td class="odd verticalLine">{{ m.servings_available }}</td>
#<td class="odd">{{ m.date_available|date:"g:i a m/d/y" }}</td>
#</tr>
#{% endfor %}
