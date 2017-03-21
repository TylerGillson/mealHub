from django.contrib import admin

from .models import Profile, MealRequest, Ingredient, Meal

admin.site.register(Profile)
admin.site.register(MealRequest)
admin.site.register(Ingredient)
admin.site.register(Meal)
