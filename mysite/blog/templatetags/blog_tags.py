from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

# registering my own template
register = template.Library()


# registering custom filter
@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


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
