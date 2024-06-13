from django.urls import path
from .import views
urlpatterns = [
    path('courses/', views.courses),
    path('', views.first_app),
    path('about/', views.about)
]
#/d/Phitron/SDT/Django/project1
#py manage.py runserver