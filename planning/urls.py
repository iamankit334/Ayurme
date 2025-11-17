from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_plan, name='generate_plan'),
    path('plan/', views.view_plan, name='view_plan'),
]
