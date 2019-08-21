from django.urls import path
from . import views

urlpatterns = [
    path('krishi/', views.current_datetime),
]
