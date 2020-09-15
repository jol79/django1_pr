from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    ###
    # post views:
    ###

    # multiple posts data:
    path('', views.post_list, name='post_list'),
    # single post data:
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail')
]
