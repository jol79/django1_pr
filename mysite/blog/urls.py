from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    ###
    # post views:
    ###

    # # multiple posts data:
    # path('', views.post_list, name='post_list'),

    # class-based view with path for multiple posts view:
    path('', views.PostListView.as_view(), name='post_list'),

    # single post data:
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),

    # email post information sharing:
    path('<int:post_id>/share/',
         views.post_share,
         name='post_share')
]
