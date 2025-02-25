from django.urls import path
from . import views


app_name = 'enquetes'

urlpatterns = [
    path('', views.enquetes, name='enquetes'),
    path('<int:id>/', views.theorie, name='theorie'),
]
