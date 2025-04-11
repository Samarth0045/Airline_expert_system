from django import forms
from .models import Flight, Cargo

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
