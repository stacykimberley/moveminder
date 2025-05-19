from django.db import models

class GymClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='class_images/')

    def __str__(self):
        return self.name
