from django.db import models

class GymClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)
    available_time_slots = models.CharField(max_length=255, default="10:00,12:00,14:00")

    def get_time_slots(self):
        return [slot.strip() for slot in self.available_time_slots.split(',')]

class Booking(models.Model):
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
