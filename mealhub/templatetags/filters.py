from django import template
from mealhub.models import Profile, Meal, MealRequest

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter(name='review_avg_whole')
def review_avg_whole(reviews):
    total = 0
    for review in reviews:
        total += review.review_rating
    avg_point_five = round((total/len(reviews)) * 2) / 2
    return int(divmod(avg_point_five,1)[0])

@register.filter(name='review_avg_part')
def review_avg_part(reviews):
    total = 0
    for review in reviews:
        total += review.review_rating
    avg_point_five = round((total/len(reviews)) * 2) / 2
    return 1 if divmod(avg_point_five,1)[1] == 0.5 else 0

@register.filter(name='empty_stars')
def empty_stars(number):
    times = 5-number
    return range(times)

@register.filter(name='times')
def times(number):
    return range(number)

@register.assignment_tag
def meal_addrs():
    meals = Meal.objects.order_by('-id')
    profiles = Profile.objects.all()
    meal_addrs = []
    for meal in meals:
        for p in profiles:
            if meal.user == p.user and p.address is not None:
                fixedName = meal.user.username.replace('.','')
                fixedMeal = meal.mealname.replace(' ','')
                meal_addrs.append((p.user,p.address + " " + p.city + " " + p.state + " " + str(p.zip_code),fixedMeal,fixedName))
    meal_addrs = set(meal_addrs)
    users = []
    newMealAddrs = []
    for x in meal_addrs:
        if x[0] not in users:
            newMealAddrs.append(x)
            users.append(x[0])
    return newMealAddrs

@register.assignment_tag
def meal_request_addrs():
    meal_requests = MealRequest.objects.order_by('-id')
    profiles = Profile.objects.all()
    fixedName = meal_requests[0].user.username.replace('.','')
    fixedRequest = meal_requests[0].mealRequestName.replace(' ','')
    meal_request_addrs = []
    for meal_request in meal_requests:
        for p in profiles:
            if meal_request.user == p.user and p.address is not None:
                meal_request_addrs.append((p.user,p.address + " " + p.city + " " + p.state + " " + str(p.zip_code),fixedRequest,fixedName))
    meal_request_addrs = set(meal_request_addrs)
    users = []
    newMealRequestAddrs = []
    for x in meal_request_addrs:
        if x[0] not in users:
            newMealRequestAddrs.append(x)
            users.append(x[0])
    return newMealRequestAddrs
