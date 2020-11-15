from django.shortcuts import render

from blog.models import Post, Category


def index(request):
    posts = Post.objects.filter(post_main_header=True).order_by("-created_at")
    main_posts = posts[:5]
    main_post = main_posts[0]
    secondary_posts = main_posts[1:3]
    third_posts = main_posts[3:5]
    categories = {}
    for post in posts:
        if post.post_category not in categories:
            categories[post.post_category] = [post]
        else:
            categories[post.post_category].append(post)
    post_context = {
        'main_posts': main_posts,
        'main_post': main_post,
        'secondary_posts': secondary_posts,
        'third_posts': third_posts,
        'categories': categories
    }
    return render(request, 'blog/index.html', post_context)


def template(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'blog/post_template.html', context)


def category_list(request, category_id):
    category = Category.objects.get(id=category_id)
    category_posts = Post.objects.filter(post_category=category)
    context = {
        'posts': category_posts,
        'category': category,
        'categories': Category.objects.all()
    }
    return render(request, 'blog/category_list.html', context)
