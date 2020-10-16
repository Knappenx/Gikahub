from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = Post.objects.filter(post_main_header=True).order_by("-created_at")
    main_posts = posts[:5]
    main_post = main_posts[0]
    secondary_posts = main_posts[1:3]
    third_posts = main_posts[3:5]
    post_context = {
        'main_posts': main_posts,
        'main_post': main_post,
        'secondary_posts': secondary_posts,
        'third_posts': third_posts
    }
    return render(request, 'blog/index.html', post_context)
