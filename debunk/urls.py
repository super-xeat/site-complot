from django.urls import path
from . import views

app_name = 'debunk'

urlpatterns = [
    path('debunk', views.debunk, name='debunk'),
    path('<int:id>/', views.explication, name='explication'),
    path('ajouter_commentaire/<int:id>/', views.ajouter_commentaire, name='ajouter_commentaire'),
]