from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommandeForm, JoueurDeChampForm, GardienForm, PersonnelDEntrainementForm
from .models import Commande, JoueurDeChamp, Calibre, Gardien, PersonnelDEntrainement
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory


@login_required
def modifier_commande(request):
    return render(request, 'commandeCLUB/modifier_commande.html')

@login_required
def historique_commandes(request):
    commandes = Commande.objects.filter(utilisateur=request.user)
    return render(request, 'commandeCLUB/historique_commandes.html', {'commandes': commandes})

@login_required
def commande_view(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            commande.utilisateur = request.user
            commande.save()
            return redirect('commandeCLUB:joueur_de_champ_form_with_id', commande_id=commande.id)
    else:
        form = CommandeForm()
    return render(request, 'commandeCLUB/formulaire.html', {'form': form})

@login_required
def hub_accueil(request):
    return render(request, 'commandeCLUB/hub_accueil.html')

@login_required
def joueur_de_champ_form_view(request, commande_id, num_champs=1):
    JoueurDeChampFormSet = formset_factory(JoueurDeChampForm, extra=num_champs)
    
    commande = get_object_or_404(Commande, id=commande_id)
    calibre = commande.calibre

    if request.method == 'POST':
        formset = JoueurDeChampFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                joueur = JoueurDeChamp()
                joueur.commande = commande

                if calibre.has_maillot_local:
                    joueur.taille = form.cleaned_data['maillot_local_taille']
                    joueur.numero = form.cleaned_data['maillot_local_numero']
                    joueur.nom = form.cleaned_data['maillot_local_nom']

                if calibre.has_maillot_visiteur:
                    joueur.maillot_visiteur_taille = form.cleaned_data['maillot_visiteur_taille']
                    joueur.maillot_visiteur_numero = form.cleaned_data['maillot_visiteur_numero']
                    joueur.maillot_visiteur_nom = form.cleaned_data['maillot_visiteur_nom']

                if calibre.has_short_local:
                    joueur.short_local_taille = form.cleaned_data['short_local_taille']

                if calibre.has_short_visiteur:
                    joueur.short_visiteur_taille = form.cleaned_data['short_visiteur_taille']

                if calibre.has_chaussettes_local:
                    joueur.chaussettes_local_taille = form.cleaned_data['chaussettes_local_taille']

                joueur.save()

            return redirect('commandeCLUB:hub_accueil')
    else:
        formset = JoueurDeChampFormSet()

    


    return render(request, 'commandeCLUB/joueur_de_champ_form.html', {'formset': formset, 'calibre': calibre, 'commande': commande})
def liste_personnel(request):
    all_personnel = PersonnelDEntrainement.objects.all()
    return render(request, 'liste_personnel.html', {'personnel': all_personnel})

def detail_personnel(request, personnel_id):
    personnel = get_object_or_404(PersonnelDEntrainement, pk=personnel_id)
    return render(request, 'detail_personnel.html', {'personnel': personnel})

def ajouter_personnel(request):
    if request.method == 'POST':
        form = PersonnelDEntrainementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_personnel')
    else:
        form = PersonnelDEntrainementForm()
    return render(request, 'form_personnel.html', {'form': form})

def modifier_personnel(request, personnel_id):
    personnel = get_object_or_404(PersonnelDEntrainement, pk=personnel_id)
    if request.method == 'POST':
        form = PersonnelDEntrainementForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('detail_personnel', personnel_id=personnel.id)
    else:
        form = PersonnelDEntrainementForm(instance=personnel)
    return render(request, 'form_personnel.html', {'form': form})








def liste_gardiens(request):
    gardiens = Gardien.objects.all()
    return render(request, 'liste_gardiens.html', {'gardiens': gardiens})

def detail_gardien(request, gardien_id):
    gardien = get_object_or_404(Gardien, pk=gardien_id)
    return render(request, 'detail_gardien.html', {'gardien': gardien})

def ajouter_gardien(request):
    if request.method == 'POST':
        form = GardienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_gardiens')
    else:
        form = GardienForm()
    return render(request, 'form_gardien.html', {'form': form})

def modifier_gardien(request, gardien_id):
    gardien = get_object_or_404(Gardien, pk=gardien_id)
    if request.method == 'POST':
        form = GardienForm(request.POST, instance=gardien)
        if form.is_valid():
            form.save()
            return redirect('detail_gardien', gardien_id=gardien.id)
    else:
        form = GardienForm(instance=gardien)
    return render(request, 'form_gardien.html', {'form': form})
