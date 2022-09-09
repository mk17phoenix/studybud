from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('room/',room),
    path('room/<str:pk>',room),
    path('update_room/<str:pk>',updateRoom,name='update-room'), 
    path('delete_room/<str:pk>',deleteRoom,name='delete-room'), 
    path('create_room/',createRoom,name='create-room') 
    ]