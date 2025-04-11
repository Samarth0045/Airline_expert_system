from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('flights/', views.flight_list, name='flight-list'),
    path('cargo/', views.cargo_list, name='cargo-list'),
    path('add-flight/', views.add_flight, name='add-flight'),
    path('add-cargo/', views.add_cargo, name='add-cargo'),
    path('chat/', views.chat, name='chat'),
]
