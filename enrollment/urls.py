from django.urls import path
from . import views
from .views import get_lgas

urlpatterns = [
    path("", views.index, name= "index"),
    path("enroll/", views.enroll, name="enroll"),
    path('get-lgas/<state_name>/', get_lgas, name='get_lgas'),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('success/', views.success, name="success"),
]