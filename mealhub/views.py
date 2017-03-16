from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

# Create your views here.
class LoginView(generic.ListView):
    template_name = 'mealhub/login.html'

def Home(request):
    return HttpResponse("Welcome to mealHub home page! :)<form action ='/users'><input type ='submit' value=\"login\" /></form>")

def RegisterView(request):
    return render(request, 'mealhub/register.html')
