# Generated by Django 4.1.2 on 2022-12-27 10:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_theme_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='parent_theme',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, to='main.theme'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_picture',
            field=models.ImageField(default=9, upload_to='communication_pictures/posts/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
