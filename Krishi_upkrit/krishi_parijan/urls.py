from django.urls import path
from . import views
app_name = 'krishi_parijan'
urlpatterns = [
    path('krishi/', views.current_datetime),
]
