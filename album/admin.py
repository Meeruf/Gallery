from django.contrib import admin

from .models import Album, Image

# Register your models here.

admin.site.register(Album)
admin.site.register(Image)



class ImageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # This is a new object, so we set the album_image_id
            max_image_id = len(Image.objects.filter(album=self.album))
            obj.album_image_id = max_image_id + 1
        super().save_model(request, obj, form, change)


    def delete_model(self, request, obj):
        album_images_after_this = Image.objects.filter(album=obj.album, album_image_id__gt=obj.album_image_id)
        super().delete_model(request, obj)
        
        # Adjust album_image_id for subsequent images
        for img in album_images_after_this:
            img.album_image_id -= 1
            img.save()