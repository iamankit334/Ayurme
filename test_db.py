import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayurveda_project.settings')
django.setup()

from django.db import connection

def check_database():
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  - {table[0]}")

    # Check some sample data
    from users.models import User
    from profiling.models import PatientProfile, PrakritiQuestion
    from nutrition.models import Recipe
    from planning.models import MealPlan

    print(f"\nUsers count: {User.objects.count()}")
    print(f"PatientProfiles count: {PatientProfile.objects.count()}")
    print(f"PrakritiQuestions count: {PrakritiQuestion.objects.count()}")
    print(f"Recipes count: {Recipe.objects.count()}")
    print(f"MealPlans count: {MealPlan.objects.count()}")

if __name__ == "__main__":
    check_database()
