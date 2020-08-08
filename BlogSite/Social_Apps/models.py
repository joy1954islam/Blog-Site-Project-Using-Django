from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER_CHOICES = (
('M', 'Male'),
('F', 'Female'),
('P', 'Prefer not to answer'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=64, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, default='M')
    bio = models.TextField(max_length=1024, null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='profile/', null=True, blank=True)




