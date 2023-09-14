from django.shortcuts import render
from django.http import Http404


def index(request):
    template = 'blog/index.html'
    context = {'posts_list': reversed(posts)}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    try:
        context = {'post': posts[post_id]}
    except IndexError:
        raise Http404('Post does not exist')

    return render(request, template, context)


def category_posts(request, slug):
    template = 'blog/category.html'
    context = {'slug': slug}
    return render(request, template, context)
