from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomUserForm, CustomForm
from .models import CustomUser




def inscription(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    else:
        form = CustomUserForm()
    return render(request, 'registration/inscription.html', {'form':form})


def auto_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.POST.get("next", "/"))
        else: 
            return render(request, "accueil.html", {"error": "Identifiants ou mot de passe incorrects"})  
    return redirect("/")    


def deconnexion(request):
    logout(request)
    return redirect(request.GET.get("next", "/"))



@login_required
def profil(request): 
    user = request.user
    if request.method == "POST" and "delete_account" in request.POST:
        user.delete()  # Supprime le compte utilisateur
        logout(request)  # Déconnecte l'utilisateur après la suppression
        return redirect("accueil")  # Redirige vers la page d'accueil après la suppression

    if request.method == "POST":
        form = CustomForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:profil")

    else:
        form = CustomForm(instance=request.user)

    return render(request, "registration/profil.html", {"form": form, "profil": request.user})














