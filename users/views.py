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
    context = {'mealrequests': mealrequest,}
    return render(request, 'users/chef.html', context)


def MouthsView(request):
    meal = Meal.objects.order_by('-date_available')
    context = {'meal': meal,}
    return render(request, 'users/mouth.html', context)

def RegisterView(request):
    return render(request, 'users/register.html')
