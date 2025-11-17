from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import PatientProfile

# Unregister the default User admin
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'location', 'dominant_dosha', 'health_goals_short')
    list_filter = ('gender', 'dominant_dosha', 'location')
    search_fields = ('user__username', 'user__email', 'location', 'dominant_dosha')
    readonly_fields = ('user',)
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'age', 'gender', 'location')
        }),
        ('Ayurvedic Profile', {
            'fields': ('dominant_dosha', 'health_goals'),
            'classes': ('collapse',)
        }),
    )

    def health_goals_short(self, obj):
        if obj.health_goals:
            return obj.health_goals[:50] + '...' if len(obj.health_goals) > 50 else obj.health_goals
        return '-'
    health_goals_short.short_description = 'Health Goals'
