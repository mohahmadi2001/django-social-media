# Generated by Django 4.2.5 on 2023-09-15 12:39

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_online', models.BooleanField(verbose_name='is_online')),
                ('bio', models.CharField(blank=True, max_length=50, null=True, verbose_name='bio')),
                ('date_of_birth', models.DateField(verbose_name='date_of_birth')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics', verbose_name='image')),
                ('following', models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL, verbose_name='following')),
                ('friends', models.ManyToManyField(blank=True, related_name='my_friends', to=settings.AUTH_USER_MODEL, verbose_name='friends')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], max_length=8, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_receiver', to='accounts.profile', verbose_name='receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_sender', to='accounts.profile', verbose_name='sender')),
            ],
            options={
                'verbose_name': 'Relationship',
                'verbose_name_plural': 'Relationships',
            },
        ),
    ]
