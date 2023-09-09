from django.db import models
from django.contrib.auth.models import User

# Create your models here.

import random, string

def generate_html_name():
    name = ''
    for _ in range(0, 6):
        name += random.choice(string.ascii_letters)
    return name


class Album(models.Model):
    title = models.CharField(max_length=255)

    custumer = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)

    http_name = models.CharField(max_length=8, default=generate_html_name)

    pin_code = models.IntegerField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Image(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sequence = models.IntegerField(null=True, blank=True)

    heart = models.BooleanField(default=False)
    photographer_comment = models.TextField(null=True, blank=True)
    costumer_comment = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to='images/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    album_image_id = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.album.title} ({self.image})'

    def save(self, *args, **kwargs):
        if not self.pk:
            max_image_id = len(Image.objects.filter(album=self.album))
            self.album_image_id = (max_image_id or 0) + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        album_images_after_this = Image.objects.filter(album=self.album, album_image_id__gt=self.album_image_id)
        super().delete(*args, **kwargs)
        
        # Adjust album_image_id for subsequent images
        for img in album_images_after_this:
            img.album_image_id -= 1
            img.save()
    