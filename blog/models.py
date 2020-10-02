from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Year(models.Model):
    current_year = date.today().year

    def __str__(self):
        return self.current_year


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=False)
    post_title = models.CharField(max_length=50, blank=True, null=True)
    post_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    post_tags = models.ManyToManyField(Tags)
    post_abstract = models.CharField(max_length=500, blank=True, null=True)
    post_slug = models.SlugField(max_length=60)
    post_main_image = models.URLField()
    post_is_draft = models.BooleanField(default=True)
    post_view_counts = models.IntegerField(default=0)
    post_main_header = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.post_title} - {self.post_category}'
