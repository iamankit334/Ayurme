from django.db import models
from users.models import PatientProfile
from nutrition.models import Recipe

class MealPlan(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=10, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
