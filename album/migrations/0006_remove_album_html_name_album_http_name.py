# Generated by Django 4.2.5 on 2023-09-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_album_html_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='html_name',
        ),
        migrations.AddField(
            model_name='album',
            name='http_name',
            field=models.CharField(default='duTeTz', max_length=8),
        ),
    ]
