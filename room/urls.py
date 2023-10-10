from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),  # Existing URL for listing rooms
    path('create/', views.create_room_view, name='create_room'),  # New URL for creating a room
    path('<slug:slug>/', views.room, name='room'),  # Existing URL for viewing a room
    
]
