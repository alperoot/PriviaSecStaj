from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    post_icerik = models.TextField()
    post_title = models.CharField(max_length=100, default='Başlık')
    date_posted = models.DateTimeField('paylaşım tarihi', default=datetime.datetime.now())
    original_poster = models.CharField(max_length=200, default='anonymous')
    comments_status = models.IntegerField(default=1)
    comments_number = models.IntegerField(default=0)
    def __str__(self):
        return self.post_icerik

class Comment(models.Model):
    comment_icerik = models.TextField()
    date_posted = models.DateTimeField('yorum tarihi')
    original_commenter = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.comment_icerik

class Status(models.Model):
    status_icerik = models.CharField(max_length=100, default="Yeni Üye")
    status_user = models.CharField(max_length=200, default="admin")
    def __str__(self):
        return self.status_icerik