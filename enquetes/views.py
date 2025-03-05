from django.shortcuts import render, get_object_or_404, redirect
from .models import Theorie, Commentaire
from .forms import CommentaireForm
from django.contrib.auth.decorators import login_required




def enquetes(request):
    theories = Theorie.objects.all()
    return render(request, 'enquetes/liste_theories.html', {'theories': theories})


def theorie(request, id):
    theorie_detail = get_object_or_404(Theorie, id=id)  
    commentaires = Commentaire.objects.filter(theorie=theorie_detail).order_by('date_publication')
    form = CommentaireForm()
    return render(request, 'enquetes/theorie.html', {'theorie': theorie_detail, 'commentaires': commentaires, 'form': form})


@login_required
def ajouter_commentaire(request, id):
    theorie = get_object_or_404(Theorie, id=id)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user # Associer au profil de l'utilisateur
            commentaire.theorie = theorie
            commentaire.save()
            
            return redirect('enquetes:theorie', id=theorie.id)

    return redirect('enquetes:theorie', id=theorie.id)
    

