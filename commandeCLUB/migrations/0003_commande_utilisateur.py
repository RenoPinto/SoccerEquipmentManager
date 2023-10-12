# Generated by Django 4.2.6 on 2023-10-06 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commandeCLUB', '0002_article_club_couleur_taille_remove_commande_nom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
