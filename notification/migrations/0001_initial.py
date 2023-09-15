# Generated by Django 4.2.5 on 2023-09-15 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_preview', models.CharField(max_length=120, verbose_name='text_preview')),
                ('is_seen', models.BooleanField(default=False, verbose_name='is_seen')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='notify_date')),
                ('notification_type', models.IntegerField(choices=[(1, 'Like'), (2, 'Follow'), (3, 'Comment'), (4, 'Reply'), (5, 'Like-Comment'), (6, 'Like-Reply')], verbose_name='notify_type')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_notifications', to='blog.post', verbose_name='post')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_receivers', to=settings.AUTH_USER_MODEL, verbose_name='receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_senders', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]
