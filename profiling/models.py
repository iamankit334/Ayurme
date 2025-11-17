from django.db import models
from users.models import PatientProfile

class PrakritiQuestion(models.Model):
    question_text = models.TextField()
    dosha = models.CharField(max_length=10, choices=[('Vata', 'Vata'), ('Pitta', 'Pitta'), ('Kapha', 'Kapha')])

class PatientResponse(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(PrakritiQuestion, on_delete=models.CASCADE)
    answer = models.IntegerField()  # Assuming Likert scale 1-5

class FoodPreference(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    preference_type = models.CharField(max_length=10, choices=[('Allergy', 'Allergy'), ('Favorite', 'Favorite'), ('Dislike', 'Dislike')])
