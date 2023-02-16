from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

import logging
logger = logging.getLogger(__name__)
"""
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.exception("An exception occured")
"""
# Create your views here.

@cache_page(30)
@vary_on_cookie
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})



def post_detail(request, slug):
    logger.warning("This is a warning message %s %s", slug, request.user)
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_active:
            if request.method == "POST":
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.content_object = post
                    comment.creator = request.user
                    comment.save()
                    return redirect(request.path_info)
            else:
                comment_form = CommentForm()
    else:
        comment_form = None
    
    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})
