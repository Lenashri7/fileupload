from django.urls import path
from .views import upload_image_view  # Import the view

urlpatterns = [
    path('', upload_image_view, name='upload'),  # Correctly define the URL
]
