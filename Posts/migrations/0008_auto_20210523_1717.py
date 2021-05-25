# Generated by Django 3.2.3 on 2021-05-23 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0007_alter_comment_comment_icerik'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='comment',
            name='date_commented',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 17, 17, 33, 95703), verbose_name='yorum tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 17, 17, 33, 95703), verbose_name='paylaşım tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='original_poster',
            field=models.CharField(default='anonymous', max_length=200),
        ),
    ]