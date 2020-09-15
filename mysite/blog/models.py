from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# creating custom manager named "publishedmanager"
class PublishedManager(models.Manager):
    ###
    # custom method to retrieve data from db
    # previously method named as "get_queryset"
    # but because of our overriding it now
    # known as "filter" method of our custom
    # manager "published"
    ###
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # for each post will be attached title
    title = models.CharField(max_length=250)

    # for each post will be attached slug:
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')

    ###
    # many-to-one db relation because each user
    # can create one or more posts, at the same
    # moment each post can have only one publisher
    # - attributes:
    #   1) CASCADE -> means that all related data with
    #   user will be deleted once user will be deleted
    #   from "User" table
    ###
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    # body of the post:
    body = models.TextField()

    # all additional data related with post:
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    # default manager:
    objects = models.Manager()
    # custom manager:
    published = PublishedManager()

    # used to link the specific posts:
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    ###
    # metadata (e.g. you tell django to sort
    # results by the publish desc, so we need
    # to put "-" symbol before the attribute
    # we want to sort by
    ###
    class Meta:
        ordering = ['-publish']
        # I can specify custom name for db tables as below:
        # db_table = ['']

    # human-readable repr of the object:
    def __str__(self):
        return self.title
