from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PrakritiQuestion, PatientResponse, FoodPreference
from users.models import PatientProfile

@login_required
def questionnaire(request):
    questions = PrakritiQuestion.objects.all()
    if request.method == 'POST':
        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            if answer:
                PatientResponse.objects.create(
                    patient=request.user.patientprofile,
                    question=question,
                    answer=int(answer)
                )
        # Calculate dominant dosha
        dosha_scores = {'Vata': 0, 'Pitta': 0, 'Kapha': 0}
        for response in PatientResponse.objects.filter(patient=request.user.patientprofile):
            dosha_scores[response.question.dosha] += response.answer
        dominant_dosha = max(dosha_scores, key=dosha_scores.get)
        request.user.patientprofile.dominant_dosha = dominant_dosha
        request.user.patientprofile.save()
        return redirect('preferences')
    return render(request, 'profiling/questionnaire.html', {'questions': questions})

@login_required
def preferences(request):
    if request.method == 'POST':
        allergies = request.POST.get('allergies', '').split(',')
        favorites = request.POST.get('favorites', '').split(',')
        dislikes = request.POST.get('dislikes', '').split(',')
        for allergy in allergies:
            if allergy.strip():
                FoodPreference.objects.create(
                    patient=request.user.patientprofile,
                    food_name=allergy.strip(),
                    preference_type='Allergy'
                )
        for favorite in favorites:
            if favorite.strip():
                FoodPreference.objects.create(
                    patient=request.user.patientprofile,
                    food_name=favorite.strip(),
                    preference_type='Favorite'
                )
        for dislike in dislikes:
            if dislike.strip():
                FoodPreference.objects.create(
                    patient=request.user.patientprofile,
                    food_name=dislike.strip(),
                    preference_type='Dislike'
                )
        return redirect('dashboard')
    return render(request, 'profiling/preferences.html')
