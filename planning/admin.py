from django.contrib import admin
from .models import MealPlan

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'meal_type', 'recipe_name', 'recipe_dosha_info')
    list_filter = ('date', 'meal_type', 'patient__dominant_dosha')
    search_fields = ('patient__user__username', 'recipe__name', 'meal_type')
    raw_id_fields = ('patient', 'recipe')
    date_hierarchy = 'date'
    ordering = ('-date', 'meal_type')

    def recipe_name(self, obj):
        return obj.recipe.name
    recipe_name.short_description = 'Recipe'
    recipe_name.admin_order_field = 'recipe__name'

    def recipe_dosha_info(self, obj):
        pacifies = obj.recipe.pacifies or 'N/A'
        aggravates = obj.recipe.aggravates or 'N/A'
        return f"Pacifies: {pacifies} | Aggravates: {aggravates}"
    recipe_dosha_info.short_description = 'Dosha Info'
