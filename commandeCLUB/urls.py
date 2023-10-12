from django.urls import path
from . import views

app_name = 'commandeCLUB'

urlpatterns = [
    path('commande/', views.commande_view, name='commande'),
    path('hub_accueil/', views.hub_accueil, name='hub_accueil'),
    path('modifier_commande/', views.modifier_commande, name='modifier_commande'),
    path('historique_commandes/', views.historique_commandes, name='historique_commandes'),

    # URL pour afficher le formulaire pour une commande spécifique.
    path('joueur_de_champ_form/<int:commande_id>/', views.joueur_de_champ_form_view, name='joueur_de_champ_form_with_id'),

    # URL pour afficher le formulaire pour une commande spécifique avec un nombre spécifié de champs.
    path('joueur_de_champ_form/<int:commande_id>/<int:num_champs>/', views.joueur_de_champ_form_view, name='joueur_de_champ_form_num'),
    
    path('gardiens/', views.liste_gardiens, name='liste_gardiens'),
    path('gardiens/<int:gardien_id>/', views.detail_gardien, name='detail_gardien'),
    path('gardiens/ajouter/', views.ajouter_gardien, name='ajouter_gardien'),
    path('gardiens/modifier/<int:gardien_id>/', views.modifier_gardien, name='modifier_gardien'),

    path('personnel/', views.liste_personnel, name='liste_personnel'),
    path('personnel/<int:personnel_id>/', views.detail_personnel, name='detail_personnel'),
    path('personnel/ajouter/', views.ajouter_personnel, name='ajouter_personnel'),
    path('personnel/modifier/<int:personnel_id>/', views.modifier_personnel, name='modifier_personnel'),
    # ... autres URL patterns ...
]
