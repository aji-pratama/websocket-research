from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html', {})


def terminal(request):
    return render(request, 'app/terminal.html', {})


def room(request, room_name):
    return render(request, 'app/room.html', {
        'room_name': room_name
    })