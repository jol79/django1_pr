from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def post_list(request):
    object_list = Post.published.all()
    # 5 posts are allowed on one page
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    ###
    # if the page is not an integer, go to the first page:
    ###
    except PageNotAnInteger:
        posts = paginator.page(1)
    ###
    # if page out of range, opens the last page with res:
    ###
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    # print single post info:
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
