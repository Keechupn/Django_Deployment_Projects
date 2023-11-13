from django.urls import path
from . import views

urlpatterns = [
    path('AgePredictionView/', views.AgePredictionView, name= 'AgePredictionView'),
]
