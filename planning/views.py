from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
import random
from .models import MealPlan
from nutrition.models import Recipe
from profiling.models import FoodPreference

@login_required
def generate_plan(request):
    patient = request.user.patientprofile
    dosha = patient.dominant_dosha

    # Check if user has completed dosha assessment
    if not dosha:
        return render(request, 'planning/generate_plan.html', {
            'error': 'Please complete your dosha assessment first.',
            'redirect_url': 'questionnaire'
        })

    # Get food preferences
    allergies = FoodPreference.objects.filter(patient=patient, preference_type='Allergy').values_list('food_name', flat=True)
    favorites = FoodPreference.objects.filter(patient=patient, preference_type='Favorite').values_list('food_name', flat=True)
    dislikes = FoodPreference.objects.filter(patient=patient, preference_type='Dislike').values_list('food_name', flat=True)

    # Generate plan for today
    today = date.today()
    meal_types = ['Breakfast', 'Lunch', 'Dinner']

    # Clear existing plans for today
    MealPlan.objects.filter(patient=patient, date=today).delete()

    generated_meals = []

    for meal_type in meal_types:
        # Priority 1: Recipes that pacify the dosha and are in favorites
        favorite_recipes = Recipe.objects.filter(
            pacifies__icontains=dosha,
            meal_time=meal_type,
            name__in=favorites
        )
        if allergies:
            favorite_recipes = favorite_recipes.exclude(
                recipe_text__icontains=','.join(allergies)
            )

        # Priority 2: Recipes that pacify the dosha but exclude dislikes
        pacifying_recipes = Recipe.objects.filter(
            pacifies__icontains=dosha,
            meal_time=meal_type
        ).exclude(
            name__in=dislikes
        )
        if allergies:
            pacifying_recipes = pacifying_recipes.exclude(
                recipe_text__icontains=','.join(allergies)
            )

        # Combine favorites first, then other pacifying recipes
        recipes = list(favorite_recipes) + list(pacifying_recipes.exclude(name__in=[r.name for r in favorite_recipes]))[:4]  # Select up to 4 options

        # Randomize the selection of recipes
        if len(recipes) > 2:
            recipes = random.sample(recipes, 2)
        else:
            recipes = recipes[:2]

        meal_recipes = []
        for recipe in recipes:
            meal_plan = MealPlan.objects.create(
                patient=patient,
                date=today,
                meal_type=meal_type,
                recipe=recipe
            )
            meal_recipes.append(recipe)

        generated_meals.append({
            'meal_type': meal_type,
            'recipes': meal_recipes
        })

    return render(request, 'planning/generate_plan.html', {
        'generated_meals': generated_meals,
        'dosha': dosha,
        'success': True
    })

@login_required
def view_plan(request):
    patient = request.user.patientprofile
    today = date.today()
    plans = MealPlan.objects.filter(patient=patient, date=today)
    return render(request, 'planning/view_plan.html', {'plans': plans})
