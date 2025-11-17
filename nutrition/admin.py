from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal_time', 'food_type', 'pacifies', 'aggravates', 'specific_conditions_short')
    list_filter = ('meal_time', 'food_type', 'pacifies', 'aggravates')
    search_fields = ('name', 'recipe_text', 'specific_conditions', 'pacifies', 'aggravates')
    readonly_fields = ('id',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'image', 'recipe_text')
        }),
        ('Meal Details', {
            'fields': ('meal_time', 'food_type')
        }),
        ('Ayurvedic Properties', {
            'fields': ('pacifies', 'aggravates', 'specific_conditions'),
            'classes': ('collapse',)
        }),
    )

    def specific_conditions_short(self, obj):
        if obj.specific_conditions:
            return obj.specific_conditions[:50] + '...' if len(obj.specific_conditions) > 50 else obj.specific_conditions
        return '-'
    specific_conditions_short.short_description = 'Conditions'
