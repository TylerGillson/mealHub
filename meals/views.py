from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Meal
from users.models import MealRequest

def SearchView(request):
    meal = Meal.objects.order_by('-date_available')
    meal_request = MealRequest.objects.order_by('-date_requested')
    context = {'meal': meal,'meal_request': meal_request, }
    return render(request, 'meals/search.html', context)
