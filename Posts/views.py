from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserForm, ToggleForm
import datetime


# Create your views here.

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'basliklar/detail.html', {'post': post})

def current_user(request):
    return request.user

def toggle_thread(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.original_poster = request.post.username
            instance.date_posted = request.post.date_posted
            instance.post_icerik = request.post.post_icerik
            instance.comments_number = request.post.comments_number
            instance.post_title = request.request.post.post_title
            if instance.comment_status == 1:
                instance.comment_status = 0
            else:
                instance.comment_status = 1
            instance.save()
            # read the doc for `redirect` and change the destination to
            # something that makes sense for your app.
            # as to why we redirect, cf  https://en.wikipedia.org/wiki/Post/Redirect/Get
            return redirect("/basliklar/gonderi/" + request.post.id)

    else:
        # GET request, present an empty form
        form = PostForm()
    return render(request, 'basliklar/gonderi.html', {"commentform": form})


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

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    flush_comments(post_id)
    post.delete()
    return redirect("/basliklar")

def flush_comments(post_id):
    post = Post.objects.get(id=post_id)
    for comment in post.comment_set.all():
        if comment.post == post:
            comment.delete()

def publish_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST' and 'publishcomment' in request.POST:
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
                post.save()
                instance.save()
                return redirect("/basliklar/" + str(post_id))
    elif request.method == 'POST' and 'togglethread' in request.POST:
        form2 = ToggleForm(request.POST)
        if form2.is_valid():
            post = Post.objects.get(id=post_id)
            post.toggle_comments()
            post.save()
            # read the doc for `redirect` and change the destination to
            # something that makes sense for your app.
            # as to why we redirect, cf  https://en.wikipedia.org/wiki/Post/Redirect/Get
            return redirect("/basliklar/" + str(post_id))
    else:
        form = CommentForm()
        form2 = ToggleForm()
    return render(request, "basliklar/detail.html", {"toggleform" : form2, "post" : post, "form" : form})

def update_status(request):
    latest_post_list = Post.objects.order_by('-date_posted')
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("/basliklar/")
    else:
        form = UserForm()
    return render(request, "basliklar/about.html", {"form": form, 'latest_post_list': latest_post_list})


def index(request):
    latest_post_list = Post.objects.order_by('-date_posted')
    template = loader.get_template('basliklar/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))