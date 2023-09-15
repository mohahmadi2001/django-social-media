# Generated by Django 4.2.5 on 2023-09-15 12:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('like', models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL, verbose_name='like')),
                ('save', models.ManyToManyField(blank=True, related_name='post_save', to=settings.AUTH_USER_MODEL, verbose_name='save')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='comment date')),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL, verbose_name='like')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='blog.post', verbose_name='post')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_reply', to='blog.comment', verbose_name='reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]