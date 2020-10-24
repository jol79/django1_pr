from django.contrib import admin
from .models import Post, Comment, TaggableManager


###
# customizing models are displayed:
###

# decorator perf. the same func as the admin.site.register()
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display - allows to set the seeing fields
    list_display = ("title", "slug", "author",
                    "publish", "status", )
    list_filter = ("status", "created", "publish", "author", "tags")

    ###
    # - search criteria, means that search key will
    # be in these parts, text in: body/title
    ###
    search_fields = ("title", "body")

    ###
    # - "prepopulated_fields" - means that all text
    # that will be provided in the title text-box
    # will be added in the slug text-box automatically
    ###
    prepopulated_fields = {"slug": ("title", )}

    ###
    # - dropdown feature that open new window with
    # users conf page where you search by user or
    # even add new users, depends on your preferences
    # - this feature useful when you have big amount
    #  of users registered in site db
    ###
    raw_id_fields = ("author", )
    date_hierarchy = "publish"
    ordering = ("status", "publish")


# decorator for comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
