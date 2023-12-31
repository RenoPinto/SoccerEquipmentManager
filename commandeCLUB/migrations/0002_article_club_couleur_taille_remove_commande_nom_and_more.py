# Generated by Django 4.2.6 on 2023-10-05 18:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('commandeCLUB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('maillot', 'Maillot'), ('short', 'Short'), ('chaussettes', 'Chaussettes'), ('hoodie', 'Hoodie'), ('polo', 'Polo')], max_length=50)),
                ('personnalisable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Couleur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couleur', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taille', models.CharField(choices=[('3/4', '3/4'), ('5/6', '5/6'), ('7/8', '7/8'), ('9/10', '9/10'), ('11/12', '11/12'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('3XL', '3XL'), ('4XL', '4XL'), ('5XL', '5XL')], max_length=5, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='commande',
            name='nom',
        ),
        migrations.AddField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='commande',
            name='statut',
            field=models.CharField(choices=[('nouveau', 'Nouveau'), ('modifie', 'Modifié'), ('finalise', 'Finalisé')], default='nouveau', max_length=20),
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type_utilisateur', models.CharField(choices=[('entraineur', 'Entraîneur'), ('personnel', 'Personnel')], max_length=20)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.club')),
            ],
        ),
        migrations.CreateModel(
            name='CommandeArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('personnalisation', models.CharField(blank=True, max_length=100)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.article')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.commande')),
                ('couleur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.couleur')),
                ('taille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.taille')),
            ],
        ),
        migrations.CreateModel(
            name='Calibre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.club')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='couleurs',
            field=models.ManyToManyField(blank=True, to='commandeCLUB.couleur'),
        ),
        migrations.AddField(
            model_name='article',
            name='tailles',
            field=models.ManyToManyField(to='commandeCLUB.taille'),
        ),
        migrations.AddField(
            model_name='commande',
            name='calibre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.calibre'),
        ),
        migrations.AddField(
            model_name='commande',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commandeCLUB.club'),
        ),
    ]
