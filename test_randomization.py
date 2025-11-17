#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayurveda_project.settings')
django.setup()

from planning.views import generate_plan
from django.test import RequestFactory
from django.contrib.auth.models import User
from users.models import PatientProfile
import re

def test_randomization():
    rf = RequestFactory()
    user = User.objects.filter(patientprofile__isnull=False).first()
    if not user:
        print('No user with profile found')
        return

    print('Testing randomization with correct regex:')
    recipes_selected = []
    for i in range(5):
        request = rf.get('/planning/generate_plan/')
        request.user = user
        response = generate_plan(request)
        content = str(response.content)
        # Extract recipe names from the HTML using correct regex
        recipe_matches = re.findall(r'<h5 class="meal-name">([^<]+)</h5>', content)
        recipes_selected.append(recipe_matches)
        print(f'Run {i+1}: {recipe_matches}')

    # Check if all runs have different selections
    unique_selections = len(set(tuple(r) for r in recipes_selected))
    print(f'Unique selections out of 5 runs: {unique_selections}')
    if unique_selections > 1:
        print('Randomization working - different recipes selected')
    else:
        print('Randomization not working - same recipes selected each time')

if __name__ == '__main__':
    test_randomization()
