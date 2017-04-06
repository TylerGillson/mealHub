from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

TYPE_CHOICES = (
    ('C', "Chef"),
    ('M', "Mouth"),
)

RATING_VALUE = (
    (0, "No Stars"),
    (1, "One Star"),
    (2, "Two Stars"),
    (3, "Three Stars"),
    (4, "Four Stars"),
    (5, "Five Stars"),
)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    zip_code = models.IntegerField(default = 00000)

    def __str__(self):
        return self.user.username

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mealname = models.CharField(max_length=50)
    mealdesc = models.CharField(max_length=200)
    meal_rating = models.IntegerField(choices=RATING_VALUE, default=0)
    #need to fix the date
    date_posted = models.DateTimeField(auto_now_add=True)
    date_available = models.DateTimeField(auto_now_add=True)
    servings_available = models.IntegerField(null=True)
    photo = models.ImageField(upload_to='meals/%Y/%m/%d', blank=True, default='meals/None/noimg.jpg')

    def __str__(self):
        return self.mealname

class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=25)

    def __str__(self):
        return self.ingredient_name

class Review(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    review_rating = models.IntegerField(choices=RATING_VALUE, default=0)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=255)

    def __str__(self):
        return str(self.reviewed_by)+'-'+str(self.meal)

class MealRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mealRequestName = models.CharField(max_length=50)
    date_created = models.DateTimeField(default =timezone.now)
    date_requested = models.DateTimeField(default =timezone.now)
    servings_requested = models.IntegerField(null=True)
    other = models.CharField(max_length=200)

    def __str__(self):
        return self.mealRequestName
