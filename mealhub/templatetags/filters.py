from django import template

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
