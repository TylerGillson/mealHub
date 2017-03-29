from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login
from users.models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileForm, ProfileEditForm, LoginForm
from django.contrib import messages

def home(request):
    return HttpResponse("Welcome to mealHub home page! :)<form action ='/login'><input type ='submit' value=\"login\" /></form>\
                                                         <form action ='/register'><input type ='submit' value=\"register\" /></form>")

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            profile.user_type = profile_form.cleaned_data['user_type']
            profile.zip_code = profile_form.cleaned_data['zip_code']
            profile.save()
            return render(request, 'mealhub/register_done.html', {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
            profile_form = ProfileForm()
            messages.error(request, 'Registration Error')
            return render(request, 'mealhub/register.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
        return render(request, 'mealhub/register.html', {'user_form': user_form, 'profile_form': profile_form})

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
<<<<<<< HEAD
def user_hub(request):
    return render(request, 'users/user_hub.html', {'section': 'user_hub'})
	
#SHAWNS WIP PAGE VIEWS
@login_required
def userhub(request):
	return render(request,'mealhub/userhub.html',{'section':'userhub'})
	
def aboutUs(request):
	return render(request,'mealhub/about.html',{'section':'aboutUs'})
@login_required
def settings(request):
	return render(request,'mealhub/settings.html',{'section':'settings'})
@login_required
def home(request):
	return render(request,'mealhub/home.html',{'section':'settings'})

@login_required
=======
>>>>>>> refs/remotes/origin/master
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'users/user_hub.html', {'section': 'user_hub'})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'mealhub/edit.html', {'user_form': user_form, 'profile_form': profile_form})
