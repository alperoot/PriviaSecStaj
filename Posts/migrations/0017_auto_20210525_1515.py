# Generated by Django 3.2.3 on 2021-05-25 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0016_auto_20210525_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_commented',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 25, 15, 15, 51, 743640), verbose_name='yorum tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 25, 15, 15, 51, 743640), verbose_name='paylaşım tarihi'),
        ),
    ]