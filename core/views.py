from django.shortcuts import render, HttpResponse, redirect, Http404
from django.http import Http404, HttpResponseNotAllowed

from album.models import Album, Image

# Create your views here.
def index(request):
    if request.method == 'POST':
        pin = request.POST['pincode']
        try:
            album = Album.objects.get(pin_code=pin)
        except Album.DoesNotExist:
            request.session['can_access'] = False
            pass
        else:
            request.session['can_access'] = True
            return redirect('core:gallery', http_name=album.http_name, grid='3')

    context = {}
    return render(request, 'gallery/login.html', context)


def gallery(request, http_name, grid):
    if request.session['can_access']:
        album = Album.objects.get(http_name=http_name)
        if request.method == 'POST':
            if 'grid-2' in request.POST:
                return redirect('core:gallery', http_name=http_name, grid='2')
            if 'grid-3' in request.POST:
                return redirect('core:gallery', http_name=http_name, grid='3')
            if 'grid-4' in request.POST:
                return redirect('core:gallery', http_name=http_name, grid='4')
            if 'grid-5' in request.POST:
                return redirect('core:gallery', http_name=http_name, grid='5')
            

        images = Image.objects.filter(album=album)
        context = {
            'album': album,
            'images': images,
            'len_img': len(images),
            'grid_setting': grid,
        }
    return render(request, 'gallery/gallery.html', context)