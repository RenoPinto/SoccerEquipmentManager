from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    utilise_maillot_domicile = models.BooleanField(default=True)
    utilise_maillot_visiteur = models.BooleanField(default=True)
    utilise_hoodie = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Calibre(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, related_name='calibres')
    
    # Ajout des champs booléens pour la modularité
    has_maillot_local = models.BooleanField(default=True, verbose_name="Utilise maillot local")
    has_maillot_visiteur = models.BooleanField(default=False, verbose_name="Utilise maillot visiteur")
    has_short_local = models.BooleanField(default=True, verbose_name="Utilise short local")
    has_short_visiteur = models.BooleanField(default=False, verbose_name="Utilise short visiteur")
    has_chaussettes_local = models.BooleanField(default=True, verbose_name="Utilise chaussettes local")

    def __str__(self):
        return self.nom


class Article(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Taille(models.Model):
    TAILLE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        # ... (ajoutez vos choix ici)
    ]
    taille = models.CharField(max_length=5, choices=TAILLE_CHOICES, unique=True)

    def __str__(self):
        return self.taille

class Couleur(models.Model):
    couleur_nom = models.CharField(max_length=100)

    def __str__(self):
        return self.couleur_nom

class Commande(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, related_name='commandes')
    calibre = models.ForeignKey(Calibre, on_delete=models.CASCADE, null=True, related_name='commandes_calibre')
    date_commande = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # ... le reste du modèle ...

class CommandeArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    # ... contenu inchangé ...

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='utilisateurs')

    # ... le reste du modèle ...

class JoueurDeChamp(models.Model):
    nom = models.CharField(max_length=100)
    maillot_local = models.ForeignKey(Article, related_name='maillots_locaux', on_delete=models.CASCADE, null=True, blank=True)
    maillot_visiteur = models.ForeignKey(Article, related_name='maillots_visiteurs', on_delete=models.CASCADE, null=True, blank=True)
    short = models.ForeignKey(Article, related_name='shorts', on_delete=models.CASCADE, null=True, blank=True)
    
    TAILLE_CHOICES = [
        ('35-38', '35-38'),
        ('39-42', '39-42'),
        ('43-47', '43-47'),
    ]
    taille_chaussettes = models.CharField(max_length=5, choices=TAILLE_CHOICES, default='39-42')
    chaussettes = models.ForeignKey(Article, related_name='chaussettes', on_delete=models.CASCADE, null=True, blank=True)


    # ... contenu inchangé ...

# Ajoutez ici les autres modèles pour les gardiens et le personnel d'entraînement.
class Gardien(models.Model):
    nom = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
    # Maillot
    maillot_taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True, related_name="gardien_maillot_taille")
    maillot_couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, related_name="gardien_maillot_couleur")
    maillot_type_manche = models.CharField(max_length=50, choices=[('court', 'Court'), ('long', 'Long')])
    
    # Shorts
    short_taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True, related_name="gardien_short_taille")
    short_couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, related_name="gardien_short_couleur")
    
    # Chaussettes
    chaussette_taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True, related_name="gardien_chaussette_taille")
    chaussette_couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, related_name="gardien_chaussette_couleur")

class PersonnelDEntrainement(models.Model):
    nom = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
    # Polo
    polo_taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True, related_name="polo_taille")
    polo_couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, related_name="polo_couleur")
    
    # Hoodie
    hoodie_taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True, related_name="hoodie_taille")
    hoodie_couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, related_name="hoodie_couleur")
    
    # Shorts
    short_taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True, related_name="personnel_short_taille")
    short_couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, related_name="personnel_short_couleur")
