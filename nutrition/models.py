from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(blank=True, null=True)
    recipe_text = models.TextField()
    meal_time = models.CharField(max_length=10, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')])
    food_type = models.CharField(max_length=20, choices=[('Beverage', 'Beverage'), ('Main Course', 'Main Course'), ('Side', 'Side')])

    # Ayurvedic properties
    pacifies = models.CharField(max_length=50, blank=True)  # e.g., 'Vata, Pitta'
    aggravates = models.CharField(max_length=50, blank=True)  # e.g., 'Kapha'
    specific_conditions = models.CharField(max_length=200, blank=True)  # e.g., 'Indigestion, Low Energy'
    ingredients = models.TextField(blank=True)  # Key ingredients for the recipe

    def __str__(self):
        return self.name
