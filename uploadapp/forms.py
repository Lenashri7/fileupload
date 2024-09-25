from django import forms
from .models import ImageModel

class ImageUploadForm(forms.ModelForm):
    json_file = forms.FileField()  # Field for uploading JSON files

    class Meta:
        model = ImageModel
        fields = ['image', 'json_file']
