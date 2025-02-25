from django.shortcuts import render, get_object_or_404, redirect
from .models import Explication, Commentaire
from .forms import commentaireForm

def debunk(request):
    explications = Explication.objects.all()
    return render(request, "debunk/debunk.html", {'explications': explications})

def explication(request, id):
    explication_detail = get_object_or_404(Explication, id=id)  
    commentaires = Commentaire.objects.filter(explication=explication_detail)
    if request.method == 'POST':
        form = commentaireForm(request.POST) #instances de la classe commentaireForm
        if form.is_valid():
            commentaire = form.save(commit=False)  
            commentaire.explication = explication_detail
            commentaire.save()
            
    else: 
        form = commentaireForm()
             
    return render(request, 'debunk/explication.html', {'explication': explication_detail, 'form' : form, 'commentaires': commentaires})

