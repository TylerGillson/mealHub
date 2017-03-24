from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from mealhub.forms import CreateMealForm
from .models import Profile, MealRequest
from meals.models import Meal

@login_required
def ChefsView(request):
    if request.method == 'POST':
        meal_form = CreateMealForm(request.POST, request.FILES)
        if meal_form.is_valid():
            meal_form.save(commit=False)

            new_meal = Meal.objects.create(user=request.user)
            new_meal.mealname = meal_form.cleaned_data['mealname']
            new_meal.mealdesc = meal_form.cleaned_data['mealdesc']
            #FIXME -- need to figure out date widget, otherwise form erros for daysss
            #new_meal.date_available = meal_form.cleaned_data['date_available']
            new_meal.servings_available = meal_form.cleaned_data['servings_available']
            new_meal.photo = meal_form.cleaned_data['photo']
            new_meal.save()
            return render(request, 'users/chef.html', {'meal_form': meal_form})
        else:
            meal_form = CreateMealForm()
            messages.error(request, 'Create a meal Error')
            return render(request, 'users/chef.html', {'meal_form': meal_form})

    else:
        meal_form = CreateMealForm()
        return render(request, 'users/chef.html', {'meal_form': meal_form})


def MouthsView(request):
    meal = Meal.objects.order_by('-date_available')
    context = {'meal': meal,}
    return render(request, 'users/mouth.html', context)

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
