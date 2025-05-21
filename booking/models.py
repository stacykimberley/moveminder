from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.contrib.auth.models import User


class GymClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)
    available_time_slots = models.CharField(max_length=255, default="10:00,12:00,14:00")
    max_capacity = models.PositiveIntegerField(default=10)

    def get_time_slots(self):
        return [slot.strip() for slot in self.available_time_slots.split(',')]

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('gym_class', 'email', 'date', 'time_slot') 

    def clean(self):
        super().clean()
        
        # Validate required fields before querying
        if not self.gym_class_id:
            raise ValidationError("Gym class must be set for booking.")
        if not self.date:
            raise ValidationError("Date must be set for booking.")
        if not self.time_slot:
            raise ValidationError("Time slot must be set for booking.")

        # Count existing bookings to enforce capacity limit
        existing_bookings = Booking.objects.filter(
            gym_class=self.gym_class,
            date=self.date,
            time_slot=self.time_slot
        ).count()

        if existing_bookings >= self.gym_class.max_capacity:
            raise ValidationError("This class is fully booked for the selected time slot.")

    def __str__(self):
        return f"{self.gym_class.name} booking by {self.first_name} {self.last_name} on {self.date} at {self.time_slot}"
