from django.contrib import admin

from .models import Profile, MealRequest, Meal, Review

admin.site.register(Profile)
admin.site.register(MealRequest)
admin.site.register(Meal)
admin.site.register(Review)
