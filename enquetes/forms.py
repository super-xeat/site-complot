from django.forms import ModelForm
from .models import Commentaire

class commentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['auteur','contenu']