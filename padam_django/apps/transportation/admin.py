from django.contrib import admin
from .models import BusShift, BusStop
from .forms import BusShiftForm

@admin.register(BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    form = BusShiftForm
    list_display = ('bus', 'driver', 'departure_time_display', 'arrival_time_display', 'shift_duration_display')

    def departure_time_display(self, obj):
        return obj.departure_time
    departure_time_display.short_description = 'Departure Time'

    def arrival_time_display(self, obj):
        return obj.arrival_time
    arrival_time_display.short_description = 'Arrival Time'

    def shift_duration_display(self, obj):
        duration = obj.shift_duration
        if duration:
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            return f"{hours}h {minutes}m"
        return "Duration not available"
    shift_duration_display.short_description = "Shift Duration"

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('place', 'arrival_time')
