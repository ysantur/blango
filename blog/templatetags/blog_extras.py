from django import template
from django.contrib.auth import get_user_model
from blog.models import Post

user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, current_user):

    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return "Me Myself"

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"
    return name


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:3]
    return {"title": "Son Postlar", "posts": posts}
