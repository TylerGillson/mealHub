from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader


from .models import MealRequest, User

# Create your views here.
class  LoginView(generic.ListView):
    template_name = 'users/login.html'


def ChefsView(request):
    mealrequest = MealRequest.objects.all()
    return render(request, 'users/chef.html', {'mealrequest':mealrequest})

#>>> for req in MealRequest.objects.all():
#...     print("%s requests %d servings of %s" %(req.user.username, req.servings_requested, req.mealRequestName)). 
#tyler requests 4 servings of Butter Chicken

def MouthsView(request):
    return render(request, 'users/mouth.html')

def RegisterView(request):
    return render(request, 'users/register.html')
