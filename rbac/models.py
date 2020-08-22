from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.URLField()
    twitter_acc = models.URLField(max_length=300, blank=True, null=True)
    facebook_acc = models.URLField(max_length=300, blank=True, null=True)
    instagram_acc = models.URLField(max_length=300, blank=True, null=True)
    user_bio = models.TextField(max_length=500, blank=True, null=True)
    newsletter_sub = models.BooleanField(default=False)
