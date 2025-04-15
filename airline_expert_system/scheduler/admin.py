from django.contrib import admin
from .models import Aircraft, Flight, Cargo, Distance

admin.site.register(Aircraft)
admin.site.register(Flight)
admin.site.register(Cargo)
admin.site.register(Distance)