from django import template
from ..models import Post

# registering my own template
register = template.Library()


# decorator used to register the func. as a simple tag
@register.simple_tag
# returns the number of published posts:
def total_posts():
    return Post.published.count()


#  template that will be rendered with returned values in latest_posts.html
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
