from django.db import models

# Create your models here.

class Post(models.Model):
    post_icerik = models.CharField(max_length=2000)
    post_title = models.CharField(max_length=100, default='Başlık')
    date_posted = models.DateTimeField('paylaşım tarihi')
    original_poster = models.CharField(max_length=200)
    comments_status = models.IntegerField(default=1)
    def __str__(self):
        return self.post_icerik

class Comment(models.Model):
    comment_icerik = models.CharField(max_length=2000)
    date_posted = models.DateTimeField('yorum tarihi')
    original_commenter = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.comment_icerik