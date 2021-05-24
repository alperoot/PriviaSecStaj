from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm
import datetime


# Create your views here.

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'basliklar/detail.html', {'post': post})

def current_user(request):
    return request.user

def publish_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.original_poster = request.user.username
            instance.date_posted = datetime.datetime.now()
            instance.save()
            # read the doc for `redirect` and change the destination to
            # something that makes sense for your app.
            # as to why we redirect, cf  https://en.wikipedia.org/wiki/Post/Redirect/Get
            return redirect("/basliklar")

    else:
        # GET request, present an empty form
        form = PostForm()
    return render(request, 'basliklar/gonderi.html', {"form" : form})

def publish_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if post.comments_status == 0:
                # do stuff
                print("thread locked")
            else:
                instance = form.save(commit=False)
                instance.original_commenter = request.user.username
                instance.post = post
                instance.date_commented = datetime.datetime.now()
                post.comment_added()
                instance.save()
                return redirect("/basliklar/" + str(post_id))
    else:
        form = CommentForm()
    return render(request, "basliklar/detail.html", {"form" : form, "post" : post})


def index(request):
    latest_post_list = Post.objects.order_by('-date_posted')[:5]
    template = loader.get_template('basliklar/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))
