# Generated by Django 3.2.3 on 2021-05-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments_number',
            field=models.IntegerField(default=0),
        ),
    ]
