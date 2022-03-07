from django.shortcuts import render


# Create your views here.
ROOMS = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]


def home(request):
    context = {
        'rooms': ROOMS
    }
    return render(request, 'base_app/home.html', context=context)


def room(request, pk):
    room = None
    for i in ROOMS:
        if i['id'] == int(pk):
            room = i
    context = {
        'room': room,
    }

    return render(request, 'base_app/room.html', context)
