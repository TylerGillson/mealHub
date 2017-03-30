from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateMealForm, MealRequestForm
from .models import Profile, MealRequest
from meals.models import Meal

@login_required
def UserHubView(request):
    if request.user.profile.user_type == "C":
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
                messages.success(request, new_meal.mealname + ' Posted!')
                return render(request, 'users/user_hub.html', {'meal_form': meal_form})
            else:
                meal_form = CreateMealForm()
                messages.error(request, 'Create a meal Error')
                return render(request, 'users/user_hub.html', {'meal_form': meal_form})

        else:
            meal_form = CreateMealForm()
            return render(request, 'users/user_hub.html', {'meal_form': meal_form})

    if request.user.profile.user_type == "M":
        if request.method == 'POST':
            meal_request = MealRequestForm(request.POST)
            if meal_request.is_valid():
                meal_request.save(commit=False)
                new_request = MealRequest.objects.create(user=request.user)
                new_request.mealRequestName = meal_request.cleaned_data['mealRequestName']
                new_request.servings_requested = meal_request.cleaned_data['servings_requested']
                #FIXME -- need to figure out date widget, otherwise form erros for daysss
                #new_meal.date_available = meal_form.cleaned_data['date_available']
                new_request.other = meal_request.cleaned_data['other']
                new_request.save()
                messages.success(request, new_request.mealRequestName + ' Requested!')
                return render(request, 'users/user_hub.html', {'meal_request': meal_request})
            else:
                meal_request = MealRequestForm()
                messages.error(request, 'Create a meal request Error')
                return render(request, 'users/user_hub.html', {'meal_request': meal_request})

        else:
            meal_request = MealRequestForm()
            return render(request, 'users/user_hub.html', {'meal_request': meal_request})


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
