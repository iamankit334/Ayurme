from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe

def recipes_list(request):
    query = request.GET.get('q', '')
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) |
            Q(recipe_text__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(specific_conditions__icontains=query)
        )

    return render(request, 'nutrition/recipes.html', {'recipes': recipes, 'query': query})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'nutrition/recipe_detail.html', {'recipe': recipe})
