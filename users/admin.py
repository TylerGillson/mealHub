from django.contrib import admin

from .models import User, MealRequest, Ingredient, Meal


admin.site.register(User)
admin.site.register(MealRequest)
admin.site.register(Ingredient)
admin.site.register(Meal)

