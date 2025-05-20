from django.urls import path
from .views import home
from . import views
 
urlpatterns = [
    path('', home, name='home'),  # Home page at root URL
    path('', views.home, name='home'),
    path('room/<uuid:id>/', views.room_detail, name='details'),
    
   
]








