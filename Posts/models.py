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
    def comment_added(self):
        if self.comments_status == 1:
            self.comments_number = self.comments_number + 1
        else:
            return 0
    def lock_comments(self):
        if self.comments_status == 1:
            self.comments_status = 0
            return 1
        else:
            return 0
    def unlock_comments(self):
        if self.comments_status == 0:
            self.comments_status == 1
            return 1
        else:
            return 0

class Comment(models.Model):
    comment_icerik = models.TextField(verbose_name='Yorum')
    date_commented = models.DateTimeField('yorum tarihi', default=datetime.datetime.now())
    original_commenter = models.CharField(max_length=200, default='anonymous')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.comment_icerik

class Status(models.Model):
    status_icerik = models.CharField(max_length=100, default="Yeni Üye")
    status_user = models.CharField(max_length=200, default="admin")
    def __str__(self):
        return self.status_icerik