from django.contrib import admin
from .models import Club, Calibre, Article, Taille, Couleur, Commande, CommandeArticle, Utilisateur, Gardien, PersonnelDEntrainement

@admin.register(Calibre)
class CalibreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'club',)  # Afficher le nom et le club associé dans la liste des calibres.
    search_fields = ('nom',)  # Ajouter une barre de recherche pour le nom.
admin.site.register(Article)
admin.site.register(Taille)
admin.site.register(Couleur)
admin.site.register(Commande)
admin.site.register(CommandeArticle)
admin.site.register(Utilisateur)

