# Generated by Django 4.1.7 on 2023-05-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_post_text_alter_theme_header_alter_theme_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='theme',
        ),
        migrations.AlterField(
            model_name='theme',
            name='header',
            field=models.TextField(db_index=True, max_length=200),
        ),
    ]
