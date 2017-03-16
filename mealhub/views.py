from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from .forms import UserRegistrationForm

# Create your views here.
class LoginView(generic.ListView):
    template_name = 'mealhub/login.html'

def home(request):
    return HttpResponse("Welcome to mealHub home page! :)<form action ='/users'><input type ='submit' value=\"login\" /></form>")

def registerView(request):
    return render(request, 'mealhub/register.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,'mealhub/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request,'mealhub/register.html',{'user_form': user_form})
