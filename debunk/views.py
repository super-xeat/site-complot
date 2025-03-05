from django.shortcuts import render, get_object_or_404, redirect
from .models import Explication, Commentaire
from .forms import CommentaireForm
from django.contrib.auth.decorators import login_required



def debunk(request):
    explications = Explication.objects.all()
    return render(request, "debunk/debunk.html", {'explications': explications})



def explication(request, id):
    explication_detail = get_object_or_404(Explication, id=id)  
    commentaires = Commentaire.objects.filter(explication=explication_detail)
    form = CommentaireForm()
    return render(request, 'debunk/explication.html', {'explications': explication_detail, 'commentaires':commentaires, 'form':form})


@login_required
def ajouter_commentaire(request,id):
    explications = get_object_or_404(Explication, id=id)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user  # Associer au profil de l'utilisateur
            commentaire.explication = explications
            commentaire.save()
            return redirect('debunk:explication', id=explications.id)
            
    return redirect('debunk:explication', id=explications.id)