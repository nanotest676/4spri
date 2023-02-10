from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Group, User


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    title = 'Профайл пользователя'
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = posts.count
    context = {
        'page_obj': page_obj,
        'username': username,
        'title': title,
        'count': count,
        'post': posts,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = post.author
    posts = Post.objects.filter(author=author)
    count = posts.count
    context = {
        'post': post,
        'count': count,
    }
    return render(request, 'posts/post_detail.html', context)


def create_post(request):
    return render(request, 'posts/create_post.html')


def post_edit(request):
    return render(request, 'posts/update_post.html')
