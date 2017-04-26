from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileForm, ProfileEditForm, LoginForm, CreateMealForm, MealRequestForm, CreateReviewForm, PasswordForm
from .models import Profile, Meal, MealRequest, Review
from social_django.models import UserSocialAuth

def home(request):
    meal = Meal.objects.order_by('-date_posted')
    meal_request = MealRequest.objects.order_by('-date_requested')
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
            profile.address = profile_form.cleaned_data['address']
            profile.city = profile_form.cleaned_data['city']
            profile.state = profile_form.cleaned_data['state']
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
        user_form = UserEditForm(request.POST, instance=request.user)#, data=request.POST)
        profile_form = ProfileEditForm(request.POST, instance=request.user.profile)#, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse('user_hub'))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        try:
            facebook_login = request.user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            facebook_login = None

        try:
            google_login = request.user.social_auth.get(provider='google-oauth2')
        except UserSocialAuth.DoesNotExist:
            google_login = None

        can_disconnect = (request.user.social_auth.count() > 1 or request.user.has_usable_password())

        return render(request, 'mealhub/edit.html', {'user_form': user_form, 'profile_form': profile_form,
                'google_login': google_login,
                'facebook_login': facebook_login,
                'can_disconnect': can_disconnect
                })

@login_required
def password(request):
    if request.method == 'POST':
        password_form = PasswordForm(request.POST, instance=request.user)

        if password_form.is_valid():
            request.user.set_password(password_form.cleaned_data['password'])
            request.user.save()
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('user_hub'))
    else:
        password_form = PasswordForm()
        return render(request, 'mealhub/password.html', {'password_form': password_form})

### MEALS ###

from django.conf import settings

def SearchView(request):
    meal = Meal.objects.order_by('-date_posted')
    meal_request = MealRequest.objects.order_by('-date_requested')
    settings.EASY_MAPS_USER = request.user.profile.user_type
    context = {'meal': meal, 'meal_request': meal_request,}
    return render(request, 'mealhub/search.html', context)

### USERS ###

@login_required
def UserHubView(request):
    meal = Meal.objects.order_by('-date_posted')[0:10]
    meal_request = MealRequest.objects.order_by('-date_requested')[0:10]
    if request.user.profile.user_type == 'C':
        previous_meals = [x for x in Meal.objects.all() if x.user.username == request.user.username]
        print(previous_meals)
        if request.method == 'POST':
            meal_form = CreateMealForm(request.POST, request.FILES)
            if meal_form.is_valid():
                meal_form.save(commit=False)
                new_meal = Meal.objects.create(user=request.user)
                new_meal.mealname = meal_form.cleaned_data['mealname']
                new_meal.mealdesc = meal_form.cleaned_data['mealdesc']
                new_meal.servings_available = meal_form.cleaned_data['servings_available']
                new_meal.ingredients = meal_form.cleaned_data['ingredients']
                new_meal.photo = meal_form.cleaned_data['photo']
                new_meal.date_available = meal_form.cleaned_data['date_available']
                new_meal.time_available =meal_form.cleaned_data['time_available']
                new_meal.save()
                messages.success(request, new_meal.mealname + ' Posted!')
                meal_form = CreateMealForm()
                return render(request, 'mealhub/user_hub.html', {'meal_form': meal_form, 'meal_request': meal_request, 'previous_meals': previous_meals})
            else:
                meal_form = CreateMealForm()
                messages.error(request, 'Create a meal Error')
                return render(request, 'mealhub/user_hub.html', {'meal_form': meal_form, 'meal_request': meal_request, 'previous_meals': previous_meals})

        else:
            meal_form = CreateMealForm()
            return render(request, 'mealhub/user_hub.html', {'meal_form': meal_form, 'meal_request': meal_request, 'previous_meals': previous_meals})

    elif request.user.profile.user_type == 'M':
        if request.method == 'POST':
            meal_request_form = MealRequestForm(request.POST, request.FILES)
            if meal_request_form.is_valid():
                meal_request_form.save(commit=False)
                new_request = MealRequest.objects.create(user=request.user)
                new_request.mealRequestName = meal_request_form.cleaned_data['mealRequestName']
                new_request.servings_requested = meal_request_form.cleaned_data['servings_requested']
                new_request.requested_date = meal_request_form.cleaned_data['requested_date']
                new_request.requested_time = meal_request_form.cleaned_data['requested_time']
                new_request.other = meal_request_form.cleaned_data['other']
                new_request.save()
                messages.success(request, new_request.mealRequestName + ' Requested!')
                meal_request_form = MealRequestForm()
                return render(request, 'mealhub/user_hub.html', {'meal_request_form': meal_request_form, 'meal': meal})
            else:
                meal_request_form = MealRequestForm()
                messages.error(request, 'Create a meal request Error')
                return render(request, 'mealhub/user_hub.html', {'meal_request_form': meal_request_form, 'meal': meal})

        else:
            meal_request_form = MealRequestForm()
            return render(request, 'mealhub/user_hub.html', {'meal_request_form': meal_request_form, 'meal': meal})
    else:
        return HttpResponseRedirect(reverse('edit'))

def meals(request, username, mealname):
    meals = Meal.objects.order_by('-date_posted')
    meal = [x for x in meals if x.user.username.replace('.','') == username and x.mealname.replace(' ','').replace("'", "") == mealname]
    meal = meal[0]
    try:
        ingredients = meal.ingredients.split(',')
    except:
        ingredients = ''
        pass
    all_reviews = Review.objects.order_by('-review_rating')
    reviews = [x for x in all_reviews if x.meal==meal]
    if request.method == 'POST':
        if request.user.is_authenticated() == False:
            review_form = CreateReviewForm()
            messages.error(request, 'You must be logged in!')
            return render(request, 'mealhub/meal.html', {'meal': meal, 'review_form': review_form, 'reviews': reviews, 'ingredients': ingredients})

        review_form = CreateReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.save(commit=False)
            new_review = Review.objects.create(meal=meal, reviewed_by=request.user)
            new_review.review_rating = review_form.cleaned_data['review_rating']
            new_review.review_text = review_form.cleaned_data['review_text']
            new_review.save()
            messages.success(request, 'Review Posted!')
            review_form = CreateReviewForm()
            return render(request, 'mealhub/meal.html', {'meal': meal, 'review_form': review_form, 'reviews': reviews, 'ingredients': ingredients})
        else:
            review_form = CreateReviewForm()
            messages.error(request, 'Create a Review Error')
            return render(request, 'mealhub/meal.html', {'meal': meal, 'review_form': review_form, 'reviews': reviews, 'ingredients': ingredients})
    else:
        review_form = CreateReviewForm()
        return render(request, 'mealhub/meal.html', {'meal': meal, 'review_form': review_form, 'reviews': reviews, 'ingredients': ingredients})

def meal_requests(request, username, meal_request_name):
    meal_requests = MealRequest.objects.order_by('-date_requested')
    meal_request = [x for x in meal_requests if x.user.username.replace('.','') == username and x.mealRequestName.replace(' ','').replace("'","") == meal_request_name]
    meal_request = meal_request[0]
    return(render(request, 'mealhub/meal_request.html', {'meal_request':meal_request}))
