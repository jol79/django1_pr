from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # use this page as main when opening web-site:
    path('', views.index, name='index'),

    # using prefix /post you can open this page:
    path('post/', views.individual_post, name='individual_post'),

    # url pattern for ind post page:
    # url(r'$', views.individual_post, name='individual_post__link')
]
