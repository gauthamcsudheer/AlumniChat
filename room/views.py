# room/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Room, Message
from .forms import RoomForm

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room).order_by('-date_added')[:25]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})

# ... (other imports)

@login_required
def create_room_view(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            # Set the owner of the room based on the logged-in user
            # room.owner = request.user
            room.save()
            return redirect('rooms')  # Redirect to room listing page
    else:
        form = RoomForm()

    return render(request, 'room/create_room.html', {'form': form})
