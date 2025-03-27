from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()

class TourismEvent(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date = models.DateField()
    details = models.TextField()

class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    duration = models.IntegerField()  # Duration in days

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    image_url = models.URLField()
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
