from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('about/', views.about, name='aboutPage'),
    path('form/', views.submit_form, name='submitForm'),
    path('django_Form/', views.password_validaion, name='djangoForm'),
]
