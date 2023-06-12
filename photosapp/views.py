from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import photos
from .forms import UploadForm


# Create your views here.


def index(request):
    # imports photos and save it in database
    photo = photos.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'photosapp/index.html',ctx)




def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'success' with the appropriate URL or view name
    else:
        form = UploadForm()
    
    return render(request, 'photosapp/upload.html', {'form': form})

# def download_photo(request, photo_id):
#     # Get the photo object
#     photo = get_object_or_404(photos, id=photo_id)

#     # Set the appropriate response headers for file download
#     response = HttpResponse(photo.image.read(), content_type='image/jpeg')
#     response['Content-Disposition'] = 'attachment; filename="{}"'.format(photo.image.name)

#     return response
