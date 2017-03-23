from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Meal

def SearchView(request):
    meal = Meal.objects.order_by('-date_available')
    context = {'meal': meal,}
    return render(request, 'meals/search.html', context)
