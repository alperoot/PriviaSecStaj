# Generated by Django 3.2.3 on 2021-05-21 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Posts.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='comments_status',
            field=models.IntegerField(default=1),
        ),
    ]