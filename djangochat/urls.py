# djangochat/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),  # Include the 'room' app URLs under 'rooms/'
    path('admin/', admin.site.urls),
]
