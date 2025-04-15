from django.db import models
from datetime import timedelta
import uuid

class Aircraft(models.Model):
    name = models.CharField(max_length=50)
    tail_number = models.CharField(max_length=10)
    max_cargo_weight = models.FloatField()

    def __str__(self):
        return f"{self.tail_number} ({self.name})"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    distance = models.ForeignKey('Distance', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Auto-calculate arrival_time if not set
        if self.departure_time and self.distance:
            avg_speed_kmph = 800  # Adjust based on realistic average
            hours = self.distance.distance_km / avg_speed_kmph
            flight_duration = timedelta(hours=hours)
            self.arrival_time = self.departure_time + flight_duration
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.flight_number} - {self.origin} to {self.destination}"

class Cargo(models.Model):
    cargo_id = models.CharField(max_length=10, unique=True, editable=False)
    Aircraft = models.ForeignKey('Aircraft', on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.FloatField()
    priority = models.CharField(choices=[('High', 'High'), ('Normal', 'Normal')], max_length=10)

    def __str__(self):
        return f"{self.cargo_id} - {self.description} ({self.weight} kg)"

    def save(self, *args, **kwargs):
        if not self.cargo_id:
            # Generate a unique ID like "C001", "C002", etc.
            last = Cargo.objects.order_by('-id').first()
            next_id = 1 if not last else last.id + 1
            self.cargo_id = f"C{next_id:03d}"
        super().save(*args, **kwargs)

class Distance(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance_km = models.FloatField()
    average_speed_kmph = models.FloatField(default=800)

    def __str__(self):
        return f"{self.origin} to {self.destination} - {self.distance_km} km"

    def get_duration(self):
        hours = self.distance_km / self.average_speed_kmph
        return timedelta(hours=hours)

    def get_estimated_arrival(self, departure_time):
        return departure_time + self.get_duration()