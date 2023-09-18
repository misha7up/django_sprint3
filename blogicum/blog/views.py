from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'

    post = get_object_or_404(Post, pk=post_id)

    if (
        post.pub_date > timezone.now()
        or not post.is_published
        or not post.category.is_published
    ):
        raise Http404('Публикация не найдена')

    context = {'post': post}

    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug)

    if not category.is_published:
        raise Http404('Категория не найдена')

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {'posts': posts}
    return render(request, template, context)
