from django.db import models

# models.py
class GymClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)
    available_time_slots = models.CharField(max_length=255, default="10:00,12:00,14:00")
    max_capacity = models.PositiveIntegerField(default=10)  # ✅ move this here

    def get_time_slots(self):
        return [slot.strip() for slot in self.available_time_slots.split(',')]

    def __str__(self):
        return self.name


class Booking(models.Model):
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        from django.utils.timezone import now
        from django.core.exceptions import ValidationError

        # Count bookings for this class, date, and time
        existing_bookings = Booking.objects.filter(
            gym_class=self.gym_class,
            date=self.date,
            time_slot=self.time_slot
        ).count()

        if existing_bookings >= self.gym_class.max_capacity:
            raise ValidationError("This class is fully booked for the selected time slot.")
