from django import forms
from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {'contenu': ''}
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': 'écrire le com....', 'style': 'resize:none; width: 50%; margin-left: 15px'}),
        }



