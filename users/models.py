from django.db import models

# Create your models here.
class User(models.Model):
    TYPE_CHOICES = (
        ('C',"Chef"),
        ('M',"Mouth"),
    )

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=5, choices = TYPE_CHOICES)
    regdate = models.DateTimeField()

    def __str__(self):
        return self.username
