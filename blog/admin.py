from django.contrib import admin

from .models import Post, Tags, Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tags)
