# Generated by Django 3.2.3 on 2021-05-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_icerik', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='yorum tarihi')),
                ('original_commenter', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_icerik', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='paylaşım tarihi')),
                ('original_poster', models.CharField(max_length=200)),
            ],
        ),
    ]
