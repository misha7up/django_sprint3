from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

POST_SHOW_LIMIT = 5


def get_posts():
    """Функция, возвращающая базовый набор объектов по указанным фильтрам"""
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
    ).select_related('category', 'author', 'location')


def index(request):
    """Функция для отображения главной страницы."""
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:POST_SHOW_LIMIT]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Функция для отображения отдельного поста."""

    post = get_object_or_404(get_posts(),
                             pk=post_id,
                             category__is_published=True)

    context = {'post': post}

    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Функция для отображения постов отдельной категории."""
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug,
    )

    posts = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {'category': category, 'posts': posts}
    return render(request, 'blog/category.html', context)
