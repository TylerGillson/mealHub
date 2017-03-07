from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=5)
    regdate = models.DateTimeField()

    def __str__(self):
        return self.username
