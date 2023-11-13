from django.urls import path
from . import views

urlpatterns = [
    path('age_app/', views.AgePredictionView, name= 'age_app'),
]
