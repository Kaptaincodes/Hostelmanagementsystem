from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = [
    ('male','MALE'),
    ('female','FEMALE'),
]



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_CHOICES = [
    ('male','MALE'),
    ('female','FEMALE'),
    ]

    gender = models.CharField(
        max_length=7,
       choices=GENDER_CHOICES,
       default = 'male',   
    )
    
    def __str__(self):
        return self.user.username
    