from django.contrib import admin

from .models import Profile, MealRequest, Meal, Ingredient, Review

admin.site.register(Profile)
admin.site.register(MealRequest)
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Review)
