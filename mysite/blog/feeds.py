from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


# subclass Feed class
class LatestPostFeed(Feed):
    ###
    # corresponds to the <title>, <link> and <description> RSS elements
    ###
    title = 'Sell offers'
    # reverse_lazy - generates URL for the link attribute
    link = reverse_lazy('blog:post_list')
    description = 'New sell offer'

    def items(self):
        return Post.published.all()[:5]

    # will recieve each object returned by items() and return the title/body
    def item_title(self, item): 
        return item.title

    # body will be displayed only first 30 words
    def item_description(self, item): 
        # truncatewords template filter to build the description of the blog post with the first 30 words
        return truncatewords(item.body, 30)