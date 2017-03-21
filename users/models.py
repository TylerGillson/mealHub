from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('C', "Chef"),
        ('M', "Mouth"),
    )
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    zip_code = models.IntegerField(default = 00000)

    def __str__(self):
        return self.user.username

class Meal(models.Model):
    RATING_VALUE = (
        (0, "No Stars"),
        (1, "One Star"),
        (2, "Two Stars"),
        (3, "Three Stars"),
        (4, "Four Stars"),
        (5, "Five Stars"),
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mealname = models.CharField(max_length=50)
    mealdesc = models.CharField(max_length=200)
    date_posted = models.DateTimeField()
    date_available = models.DateTimeField()
    servings_available = models.IntegerField()
    meal_rating = models.IntegerField(choices=RATING_VALUE, default=0)

    def __str__(self):
        return self.mealname

class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=25)
   # quantity = models.DecimalField(max_digits=4, decimal_places=2) #don't think i really need this

    def __str__(self):
        return self.ingredient_name
'''
class Review(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(max_length =255)

    def __str__(self):
        return ("%s Review by %s" %(self.meal.mealname, self.reviewd_by.username))
'''
class MealRequest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mealRequestName = models.CharField(max_length=50)
    date_created = models.DateTimeField(default =timezone.now)
    date_requested = models.DateTimeField(default =timezone.now)
    servings_requested = models.IntegerField()
    other = models.CharField(max_length=200) #I'm alergic to peanuts.. etc

    def __str__(self):
        return self.mealRequestName
