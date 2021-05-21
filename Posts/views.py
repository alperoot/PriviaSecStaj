from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.template import loader

# Create your views here.

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'basliklar/detail.html', {'post': post})

def comment(request, post_id):
    return HttpResponse("%s numaralı gönderiye yorum yapılıyor." % post_id)

def index(request):
    latest_post_list = Post.objects.order_by('-date_posted')[:5]
    template = loader.get_template('basliklar/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))
