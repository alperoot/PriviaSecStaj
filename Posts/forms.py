from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import User

class PostForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ("post_title", "post_icerik", "original_poster", "comments_status", "comments_number")
        widgets = {'original_poster': forms.HiddenInput(), 'comments_status': forms.HiddenInput(), 'comments_number': forms.HiddenInput()}

class CommentForm(forms.ModelForm):
    class Meta(object):
        model = Comment
        fields = ("comment_icerik", "original_commenter", "date_commented", "post")
        widgets = {'original_commenter' : forms.HiddenInput(), 'date_commented' : forms.HiddenInput(), 'post' : forms.HiddenInput()}

class UserForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ('last_name',)
        labels = {'last_name' : "Yeni durum mesajı:"}

class ToggleForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ('comments_status',)
        widgets = {'comments_status' : forms.HiddenInput}

