from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
class  LoginView(generic.ListView):
    template_name = 'users/login.html'


def ChefsView(request):
    return render(request, 'users/chef.html')

def MouthsView(request):
    return render(request, 'users/mouth.html')
