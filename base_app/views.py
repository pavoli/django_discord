from django.shortcuts import render


# Create your views here.
ROOMS = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')
