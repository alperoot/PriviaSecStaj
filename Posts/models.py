from django.db import models

# Create your models here.

class Post(models.Model):
    post_icerik = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('paylaşım tarihi')
    original_poster = models.CharField(max_length=200)
    comments_status = 1

class Comment(models.Model):
    comment_icerik = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('yorum tarihi')
    original_commenter = models.CharField(max_length=200)