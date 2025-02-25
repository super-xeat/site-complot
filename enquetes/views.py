from django.shortcuts import render, get_object_or_404
from .models import Theorie, Commentaire
from .forms import commentaireForm

# Create your views here.
def enquetes(request):
    theories = Theorie.objects.all()
    return render(request, 'enquetes/liste_theories.html', {'theories': theories})


def theorie(request, id):
    theorie_detail = get_object_or_404(Theorie, id=id)  
    commentaires = Commentaire.objects.filter(explication=theorie_detail)
    if request.method == 'POST':
        form = commentaireForm(request.POST) #instances de la classe commentaireForm
        if form.is_valid():
            commentaire = form.save(commit=False)  
            commentaire.theorie = theorie_detail  
            commentaire.save()
            
    else: 
        form = commentaireForm()
             
    return render(request, 'enquetes/theorie.html', {'theorie': theorie_detail, 'form' : form, 'commentaires': commentaires})


