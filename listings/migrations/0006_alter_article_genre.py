# Generated by Django 3.2.20 on 2023-07-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_article_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='genre',
            field=models.CharField(choices=[('Bur', 'Bureau'), ('Cui', 'Cuisine'), ('Sdb', 'Salle De Bain'), ('Sal', 'Salon'), ('Cha', 'Chambre'), ('Dec', 'Decoration')], max_length=10),
        ),
    ]
