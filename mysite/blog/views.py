from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def post_list(request):
    # print all posts using our custom created manager:
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    # print single post info:
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             publish_year=year,
                             publish_month=month,
                             publish_day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
