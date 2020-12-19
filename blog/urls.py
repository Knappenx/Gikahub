from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:id>/<post_slug>/', views.template, name='post_template'),
    path('category/<int:category_id>/', views.category_list, name='category_list'),
]
