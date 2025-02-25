from django.shortcuts import render, redirect
from debunk.models import Explication
from enquetes.models import Theorie


def home(request):
    return render(request, 'accueil.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    query = request.GET.get('q','')
    
    explication_result = Explication.objects.filter(titre__iexact=query).first()
    if explication_result:
        return redirect('debunk:explication', id=explication_result.id)
    
    theorie_result = Theorie.objects.filter(titre__iexact=query).first()   
    if theorie_result:
        return redirect('enquetes:theorie', id=theorie_result.id)