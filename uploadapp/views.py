from django.shortcuts import render, redirect
from .forms import ImageUploadForm
import json

def upload_image_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            form.save()

            # Parse the JSON file
            json_file = request.FILES['json_file']  # Ensure you are uploading a JSON file
            json_data = json.load(json_file)

            # Extract the data from the JSON
            title = json_data.get('title', '')
            name = json_data.get('name', '')
            age = json_data.get('age', '')
            location = json_data.get('location', '')

            return render(request, 'upload.html', {
                'form': form,
                'image_url': form.instance.image.url,
                'title': title,
                'name': name,
                'age': age,
                'location': location,
            })
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})
