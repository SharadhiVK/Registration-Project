from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.create_registration, name='create_registration'),
    path('registration/<int:id>/', views.get_registration, name='get_registration'),
    path('registration/<int:id>/update/', views.update_registration, name='update_registration'),
    path('registration/<int:id>/delete/', views.delete_registration, name='delete_registration'),
]
