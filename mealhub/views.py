from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from users.models import Profile
from .forms import UserForm, ProfileForm, LoginForm

class LoginView(generic.ListView):
    template_name = 'mealhub/login.html'

def home(request):
    return HttpResponse("Welcome to mealHub home page! :)<form action ='/login'><input type ='submit' value=\"login\" /></form>")

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            first_name = user_form.cleaned_data['first_name']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.is_active = False
            user.save()
        profile_form = ProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile = Profile(user=user)
            profile.user_type = profile_form.cleaned_data['user_type']
            profile.zip_code = profile_form.cleaned_data['zip_code']
            profile.save()
            return render(request,'mealhub/register_done.html',{'user': user})
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        return render(request,'mealhub/register.html',{
            'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def user_hub(request):
    return render(request, 'users/user_hub.html', {'section': 'user_hub'})
