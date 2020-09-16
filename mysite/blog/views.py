from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# def post_list(request):
#     object_list = Post.published.all()
#     # 5 posts are allowed on one page
#     paginator = Paginator(object_list, 5)
#     page = request.GET.get('page')
#
#     try:
#         posts = paginator.page(page)
#     ###
#     # if the page is not an integer, go to the first page:
#     ###
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     ###
#     # if page out of range, opens the last page with res:
#     ###
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                    'posts': posts})
from django.views.generic import ListView
from .forms import EmailPostForm


###
# class-based view, analogous to the previous post_list
# view
###
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'


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


def post_share(request, post_id):
    # form was submitted:
    post = get_object_or_404(Post,
                             id=post_id,
                             status="published")

    # if for submitted by user:
    if request.method == "POST":

        # get data from user
        form = EmailPostForm(request.POST)

        # if all text-boxes submitted
        if form.is_valid():
            # fields passed validation:
            cd = form.cleaned_data
            # send email
    else:
        form = EmailPostForm()
    return render(request,
                  "blog/post/share.html",
                  {"post": post,
                   "form": form})


