from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    billing_plan = models.CharField(max_length= 200, null= True, blank= True)
    duration = models.IntegerField(null= True, blank= True)
    