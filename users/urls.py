from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("inscription/", views.inscription, name="inscription"),
    path("auto_login/", views.auto_login, name="auto_login"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("profil/", views.profil, name='profil'),
]