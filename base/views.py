from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse

from base.models import Room
from base.forms import RoomForm

# Create your views here.

# rooms = [
#     {'id':1, 'name': 'mk17phoenix'},
#     {'id':2, 'name': 'mk17dev'},
#     {'id':3, 'name': 'mk17brand'}
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms,'time':datetime.now()}
    return render(request,'home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'room_form.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'object':room.name}
    return render(request, 'delete_room.html',context)
        