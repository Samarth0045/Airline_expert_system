from django import forms
from .models import Flight, Cargo

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'flight_number': forms.TextInput(attrs={'class': 'form-control'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'aircraft': forms.Select(attrs={'class': 'form-control'}),
            'distance': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'flight_number': 'Flight Number',
            'departure_time': 'Departure Time',
            'arrival_time': 'Arrival Time',
        }
        help_texts = {
            'flight_number': 'Enter unique flight number, e.g., AI-203.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departure_time'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['arrival_time'].input_formats = ['%Y-%m-%dT%H:%M']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
