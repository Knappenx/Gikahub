from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    #author = models.
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=False)
    post_title = models.TextField(max_length=50)
    post_category = models.Choices()
    post_tags = models.TextField(max_length=20, blank=True, null=True)
    #could show list of available ones (dropdown list with write in function)
    post_abstract =models.TextField(max_length=500, blank=True, null=True)
    post_slug = models.TextField(max_length=60, blank=True, null=True)
    #Could have suggested slug with title
    post_main_image = models.ImageField()
    post_is_draft = models.BooleanField(default=True, null=False)
    post_view_counts = models.Count()

