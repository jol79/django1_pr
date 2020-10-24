from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSiteMap(Sitemap):
    ###
    # attributes that indicate the change frequency
    # of post pages and their relevance on the web site
    ###
    chagnefreq = 'weekly'
    # max value = 1
    priority = 0.9

    def items(self):
        return Post.published.all()


    # self - instance of the class, with this I can access the attributes and methods of the class
    def lastmod(self, obj):
        return obj.updated 