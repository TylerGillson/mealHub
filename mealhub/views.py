from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileForm, ProfileEditForm, LoginForm, CreateMealForm, MealRequestForm
from .models import Profile, Meal, MealRequest

def home(request):
    meal = Meal.objects.order_by('-date_available')[0:10]
    meal_request = MealRequest.objects.order_by('-date_requested')[0:10]
    context = {'meal': meal,'meal_request': meal_request,'section':'home'}
    return render(request,'mealhub/home.html', context)

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

def aboutUs(request):
	return render(request,'mealhub/about.html',{'section':'aboutUs'})

@login_required
def settings(request):
	return render(request,'mealhub/edit.html',{'section':'settings'})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return UserHubView(request)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'mealhub/edit.html', {'user_form': user_form, 'profile_form': profile_form})

### MEALS ###

def SearchView(request):
    meal = Meal.objects.order_by('-date_available')
    meal_request = MealRequest.objects.order_by('-date_requested')
    context = {'meal': meal,'meal_request': meal_request, }
    return render(request, 'mealhub/search.html', context)

### USERS ###

@login_required
def UserHubView(request):
    meal = Meal.objects.order_by('-date_available')[0:10]
    meal_request = MealRequest.objects.order_by('-date_requested')[0:10]
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
                meal_form = CreateMealForm()
                return render(request, 'mealhub/user_hub.html', {'meal_form': meal_form, 'meal_request': meal_request})
            else:
                meal_form = CreateMealForm()
                messages.error(request, 'Create a meal Error')
                return render(request, 'mealhub/user_hub.html', {'meal_form': meal_form, 'meal_request': meal_request})

        else:
            meal_form = CreateMealForm()
            return render(request, 'mealhub/user_hub.html', {'meal_form': meal_form, 'meal_request': meal_request})

    if request.user.profile.user_type == "M":
        if request.method == 'POST':
            meal_request_form = MealRequestForm(request.POST)
            if meal_request.is_valid():
                meal_request.save(commit=False)
                new_request = MealRequest.objects.create(user=request.user)
                new_request.mealRequestName = meal_request.cleaned_data['mealRequestName']
                new_request.servings_requested = meal_request.cleaned_data['servings_requested']
                #FIXME -- need to figure out date widget, otherwise form erros for daysss
                #new_request.date_requested  = meal_form.cleaned_data['date_requested']
                new_request.other = meal_request.cleaned_data['other']
                new_request.save()
                messages.success(request, new_request.mealRequestName + ' Requested!')
                meal_request_form = MealRequestForm()
                return render(request, 'mealhub/user_hub.html', {'meal_request_form': meal_request_form, "meal": meal})
            else:
                meal_request_form = MealRequestForm()
                messages.error(request, 'Create a meal request Error')
                return render(request, 'mealhub/user_hub.html', {'meal_request_form': meal_request_form, "meal": meal})

        else:
            meal_request_form = MealRequestForm()
            return render(request, 'mealhub/user_hub.html', {'meal_request_form': meal_request_form, "meal": meal})
