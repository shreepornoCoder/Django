from django.urls import path, include
from posts import views

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete, name='delete_post'),
]
