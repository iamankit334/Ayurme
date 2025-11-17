from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PatientProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'id_username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'id_email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'id': 'id_password1'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'id_password2'})

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['age', 'gender', 'location', 'health_goals']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].widget.attrs.update({'class': 'form-control', 'id': 'id_age'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control', 'id': 'id_gender'})
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'id': 'id_location'})
        self.fields['health_goals'].widget.attrs.update({'class': 'form-control', 'id': 'id_health_goals'})
