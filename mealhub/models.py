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

US_STATES = (('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=50, choices=US_STATES, null=True)
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
    ingredients = models.CharField(max_length=2000, null=True)
    photo = models.ImageField(upload_to='meals/%Y/%m/%d', blank=True, default='meals/None/noimg.jpg')

    def __str__(self):
        return self.mealname

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
