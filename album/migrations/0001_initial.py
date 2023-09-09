# Generated by Django 4.2.5 on 2023-09-07 20:48

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
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('custumer', models.CharField(max_length=255)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sequence', models.IntegerField()),
                ('heart', models.BooleanField()),
                ('photographer_comment', models.TextField()),
                ('costumer_comment', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.album')),
            ],
        ),
    ]
