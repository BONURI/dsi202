from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tenant, Landlord, Room, Review, Booking, Admin
from django.db.models import Q  # For complex queries

from django.shortcuts import render, get_object_or_404
from .models import Room
 
# Home Page (FBV)
def home(request):
    featured_rooms = [] 
    return render(request, 'home.html', {'featured_rooms': featured_rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'room_detail.html', {'room': room})

