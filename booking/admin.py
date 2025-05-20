# admin.py
from django.contrib import admin
from .models import GymClass

@admin.register(GymClass)
class GymClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_capacity', 'current_bookings', 'is_full')
    readonly_fields = ('current_bookings', 'is_full')

    def current_bookings(self, obj):
        return obj.booking_set.count()  # Or obj.bookings.count() if related_name='bookings'

    def is_full(self, obj):
        return obj.booking_set.count() >= obj.max_capacity

    is_full.boolean = True  # Shows a ✓ or ✗ in admin list
