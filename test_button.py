from planning.views import generate_plan
from django.test import RequestFactory
from django.contrib.auth.models import User
from users.models import PatientProfile

rf = RequestFactory()
user = User.objects.filter(patientprofile__isnull=False).first()
if user:
    request = rf.get('/planning/generate_plan/')
    request.user = user
    response = generate_plan(request)
    content = str(response.content)
    if 'secondary-btn' in content and 'Browse All Recipes' in content:
        print('SUCCESS: Button has correct styling class')
    else:
        print('FAIL: Button styling class not found')
    if 'bi-book' in content and 'Browse All Recipes' in content:
        print('SUCCESS: Button has book icon')
    else:
        print('FAIL: Button icon not found')
    if 'href="/nutrition/recipes/"' in content:
        print('SUCCESS: Button has correct href')
    else:
        print('FAIL: Button href not correct')
else:
    print('No user with profile found')
