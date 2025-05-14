from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tenant, Landlord, Room, Review, Booking, Admin
from django.db.models import Q  # For complex queries
 
# Home Page (FBV)
def home(request):
    featured_rooms = [] 
    return render(request, 'home.html', {'featured_rooms': featured_rooms})