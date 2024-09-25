from django.contrib import admin
from django.urls import include, path  # Make sure to include the `include` function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('uploadapp.urls')),  # Include the URLs from your app
]
