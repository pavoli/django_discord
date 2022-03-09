from django.shortcuts import render
from .models import Room

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'base_app/home.html', context=context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        'room': room,
    }

    return render(request, 'base_app/room.html', context)
