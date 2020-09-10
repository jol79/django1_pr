from django.shortcuts import render
from django.http import HttpResponse


def individual_post(request):
    # return HttpResponse("Ola, this is ind post")
    return render(
        request,
        'index.html'
    )


def index(request):
    # return HttpResponse("Welcome on index page !!!")
    return render(
        request,
        'post.html'
    )
