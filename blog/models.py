from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)


class Tags(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=False)
    post_title = models.CharField(max_length=50, blank=True, null=True)
    post_category = models.ForeignKey(Category)
    post_tags = models.ManyToManyField(Tags)
        #could show list of available ones (dropdown list with write in function)
    post_abstract = models.CharField(max_length=500, blank=True, null=True)
    post_slug = models.SlugField(max_length=60)
        #Could have suggested slug with title
    post_main_image = models.URLField()
    post_is_draft = models.BooleanField(default=True)
    post_view_counts = models.Count() #Or use IntegerField


