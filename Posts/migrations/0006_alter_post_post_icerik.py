# Generated by Django 3.2.3 on 2021-05-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0005_post_comments_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_icerik',
            field=models.TextField(),
        ),
    ]