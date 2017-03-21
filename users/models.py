from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('C', "Chef"),
        ('M', "Mouth"),
    )
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    zip_code = models.IntegerField(default = 00000)

    def __str__(self):
        return self.user.username

class MealRequest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mealRequestName = models.CharField(max_length=50)
    date_created = models.DateTimeField(default =timezone.now)
    date_requested = models.DateTimeField(default =timezone.now)
    servings_requested = models.IntegerField()
    other = models.CharField(max_length=200) #I'm alergic to peanuts.. etc

    def __str__(self):
        return self.mealRequestName
