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
    meals = Meal.objects.all()
    profiles = Profile.objects.all()
    meal_addrs = []
    for meal in meals:
        for p in profiles:
            if meal.user == p.user and p.address is not None:
                meal_addrs.append((p.user,p.address + " " + p.city + " " + p.state + " " + str(p.zip_code)))
    meal_addrs = set(meal_addrs)
    return meal_addrs

@register.assignment_tag
def meal_request_addrs():
    meal_requests = MealRequest.objects.all()
    profiles = Profile.objects.all()
    meal_request_addrs = []
    for meal_request in meal_requests:
        for p in profiles:
            if meal_request.user == p.user and p.address is not None:
                meal_request_addrs.append((p.user,p.address + " " + p.city + " " + p.state + " " + str(p.zip_code)))
    meal_request_addrs = set(meal_request_addrs)
    return meal_request_addrs
