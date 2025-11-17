from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    location = models.CharField(max_length=100)
    dominant_dosha = models.CharField(max_length=10, choices=[('Vata', 'Vata'), ('Pitta', 'Pitta'), ('Kapha', 'Kapha')], blank=True, null=True)
    health_goals = models.TextField(blank=True, null=True)
