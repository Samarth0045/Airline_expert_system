from django.shortcuts import render, redirect
from .models import Flight, Cargo
from .forms import FlightForm, CargoForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
import random

def home(request):
    return render(request, 'scheduler/index.html')

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'scheduler/flight_list.html', {'flights': flights})

def cargo_list(request):
    cargo = Cargo.objects.all()
    return render(request, 'scheduler/cargo_list.html', {'cargo': cargo})

def add_flight(request):
    form = FlightForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('flight-list')
    return render(request, 'scheduler/add.html', {'form': form, 'title': 'Add Flight'})

def add_cargo(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cargo-list')
    return render(request, 'scheduler/add.html', {'form': form, 'title': 'Add Cargo'})

class FlightUpdateView(UpdateView):
    model = Flight
    fields = '__all__'
    template_name = 'scheduler/update_flight.html'
    success_url = reverse_lazy('flight-list')

class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'scheduler/confirm_delete.html'
    success_url = reverse_lazy('flight-list')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()

        # Load previous context
        conversation_history = request.session.get('chat_history', [])

        # Add the new message to history
        conversation_history.append(user_message)
        if len(conversation_history) > 5:
            conversation_history = conversation_history[-5:]  # Keep last 5

        # Save back to session
        request.session['chat_history'] = conversation_history

        # Base response logic
        if "flight" in user_message:
            reply = "You can view flights at <a href='/flights/'>/flights/</a> or add a new one at <a href='/add-flight/'>/add-flight/</a>."
        elif "cargo" in user_message:
            reply = "Check cargo assignments at <a href='/cargo/'>/cargo/</a> or assign new cargo at <a href='/add-cargo/'>/add-cargo/</a>."
        elif "hello" in user_message or "hi" in user_message:
            reply = "Hi there! 👋 I'm your Airline Assistant. Ask me anything about flights or cargo."
        elif "help" in user_message:
            reply = "I can help you manage flights ✈️ and cargo 📦. Try asking: 'show flights', 'add cargo', or 'how do I schedule a flight?'."
        elif "how" in user_message and "schedule" in user_message:
            reply = "To schedule a flight, go to <a href='/add-flight/'>Add Flight</a> and fill in the details."
        elif "show more" in user_message:
            if any("flight" in msg for msg in conversation_history):
                reply = "You can also manage aircrafts and timings from the admin dashboard."
            elif any("cargo" in msg for msg in conversation_history):
                reply = "Cargo tracking is coming soon! For now, use <a href='/cargo/'>View Cargo</a>."
            else:
                reply = "More about what? Try saying 'show more flights' or 'show more cargo'."
        else:
            reply = "🤖 Sorry, I didn’t get that. Try asking about flights, cargo, or type 'help'."

        return JsonResponse({"reply": reply})
