# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Post
from .forms import BlogPostForm

# Create your views here.

def post_list(request):
    """
    Create a view that will return a 
    list of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    ("__lte" means less than or equal to )
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    render it to the 'postdetail.html'
    template. Or return a 404 error if
    the post is not found
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1 # count up the number of post views
    post.save()
    return render(request, "postdetail.html", {'post': post})


def new_post(request):
    """
    Create a view that saves our post
    when the submit button is clicked
    by accessing the POST method and then
    redirects us to our new blog post
    """
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})


def edit_post(request, id):
    """
    Create a view that uses POST and GET
    methods to either give us the post we 
    want to edit in a form (GET) or to save
    the post and redirect us to the updated
    version of the post (POST)
    """
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
