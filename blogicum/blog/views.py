from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post, Category


POST_LIMIT = 5


def get_filtered_posts(manager=Post.objects):
    return (
        manager.filter(
            is_published=True,
            pub_date__lte=now(),
            category__is_published=True
        )
        .select_related(
            'category',
            'author',
            'location'
        )
        .order_by('-pub_date')
    )


def index(request):
    posts = get_filtered_posts()[:POST_LIMIT]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        get_filtered_posts(),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_filtered_posts(category.posts)
    return render(
        request,
        'blog/category.html',
        {'category': category, 'posts': posts}
    )
