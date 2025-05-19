from django.db import models

class GymClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='class_images/')
    available_time_slots = models.CharField(max_length=255)  # or use a better structure if needed

    def __str__(self):
        return self.name
