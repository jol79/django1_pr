from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector

"""
forms
"""
from .forms import EmailPostForm, CommentForm, SearchForm

"""
views
"""
from django.views.generic import ListView

"""
models
"""
from .models import Post, Comment


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


###
# class-based view, analogous to the previous post_list
# view
###
class PostListView(ListView):
    queryset = Post.published.all()
    # variable posts will keep the query results
    context_object_name = 'posts'
    paginate_by = 5
    # template to render the page
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    # print single post info:
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # list of active comments for this post:
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == "Post":
        # comment was posted:
        comment_form = CommentForm(data=request.POST)

        # check if form filled valid:
        if comment_form.is_valid():
            ###
            # create comment but not save it to the db yet
            # for situations when you want to make final
            # changes and only after that submit form:
            ###
            new_comment = comment_form.save(commit=False)
            # assign the current page to the comment:
            new_comment.post = post
            # save the comment to the db:
            new_comment.save()
    else:
        # if the method is NOT POST -> load form again
        comment_form = CommentForm()

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def post_share(request, post_id):
    # retrieve post by id:
    post = get_object_or_404(Post,
                             id=post_id,
                             status="published")
    sent = False

    if request.method == "POST":
        # form was submitted
        form = EmailPostForm(request.POST)

        ###
        # if all text-boxes submitted with valid data
        # in case if data is not valid the result of
        # is_valid is False, and form with submitted
        # data will be rendered again in the template
        ###
        if form.is_valid():
            # retrieve validated data:
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" \
                      f"{post.title}"
            message = f"Read {post.title} as {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'asdnaskdjndkajdasn@gmail.com',
                      [cd['to']])

            # variable to use in the template, needed to inform user a success message when it successfully submitted
            sent = True
    else:
        form = EmailPostForm()
    return render(request,
                  "blog/post/share.html",
                  {"post": post,
                   "form": form,
                   "sent": sent})


def post_search(request): 
    form = SearchForm()
    query = ''
    results = []

    # looking for query param in the requerst.GET dict
    if 'query' is request.GET:
        # sending form using GET method, so that the resulting URL includes the query param
        form = SearchForm(request.GET)
        if form.is_valid:
            query = form.cleaned_data['query']
            
            # results = Post.published.annotate(
            #     search = SearchVector('title', 'body'),
            # ).filter(search=query)
            results = Post.objects.filter(title__search=query)
    return render(request, 'blog/search.html',
                 {'form': form,
                 'query': query, 
                 'results': results})

