from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import PatientProfile
from .forms import PatientProfileForm, CustomUserCreationForm
from profiling.models import PatientResponse, FoodPreference
from planning.models import MealPlan

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = PatientProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = CustomUserCreationForm()
        profile_form = PatientProfileForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    profile = get_object_or_404(PatientProfile, user=request.user)

    # Get questionnaire responses
    responses = PatientResponse.objects.filter(patient=profile).select_related('question')

    # Get food preferences
    preferences = FoodPreference.objects.filter(patient=profile)

    # Get meal plans
    meal_plans = MealPlan.objects.filter(patient=profile).select_related('recipe').order_by('date', 'meal_type')

    # Group meal plans by date
    meal_plans_by_date = {}
    for plan in meal_plans:
        date_str = plan.date.strftime('%Y-%m-%d')
        if date_str not in meal_plans_by_date:
            meal_plans_by_date[date_str] = {'date': plan.date, 'meals': []}
        meal_plans_by_date[date_str]['meals'].append(plan)

    context = {
        'profile': profile,
        'responses': responses,
        'preferences': preferences,
        'meal_plans_by_date': meal_plans_by_date,
    }

    return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
    profile = get_object_or_404(PatientProfile, user=request.user)

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = PatientProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form, 'profile': profile})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        profile = PatientProfile.objects.get(user=request.user)
    except PatientProfile.DoesNotExist:
        # Create profile if it doesn't exist
        profile = PatientProfile.objects.create(user=request.user)
    return render(request, 'users/dashboard.html', {'profile': profile})
