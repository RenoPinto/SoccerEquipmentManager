from django import forms
from .models import Commande
from .models import Gardien, PersonnelDEntrainement

CHOICES_TAILLE = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large')
]

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'

class MaillotForm(forms.Form):
    taille = forms.ChoiceField(choices=CHOICES_TAILLE)
    numero = forms.IntegerField()
    nom = forms.CharField(max_length=100)

class ShortForm(forms.Form):
    quantite = forms.IntegerField()
    taille = forms.ChoiceField(choices=CHOICES_TAILLE)

class ChaussettesForm(forms.Form):
    quantite = forms.IntegerField()
    taille = forms.ChoiceField(choices=CHOICES_TAILLE)

class JoueurDeChampForm(forms.Form):
    maillot_local_taille = forms.ChoiceField(choices=CHOICES_TAILLE, label="Taille du maillot local")
    maillot_local_numero = forms.IntegerField(label="Numéro du maillot local")
    maillot_local_nom = forms.CharField(max_length=100, label="Nom sur le maillot local")
    
    maillot_visiteur_taille = forms.ChoiceField(choices=CHOICES_TAILLE, label="Taille du maillot visiteur", required=False)
    maillot_visiteur_numero = forms.IntegerField(label="Numéro du maillot visiteur", required=False)
    maillot_visiteur_nom = forms.CharField(max_length=100, label="Nom sur le maillot visiteur", required=False)
    
    short_local_taille = forms.ChoiceField(choices=CHOICES_TAILLE, label="Taille du short local")
    short_visiteur_taille = forms.ChoiceField(choices=CHOICES_TAILLE, label="Taille du short visiteur", required=False)
    
    chaussettes_local_taille = forms.ChoiceField(choices=CHOICES_TAILLE, label="Taille des chaussettes locales")



class GardienForm(forms.ModelForm):
    class Meta:
        model = Gardien
        fields = '__all__'

class PersonnelDEntrainementForm(forms.ModelForm):
    class Meta:
        model = PersonnelDEntrainement
        fields = '__all__'
