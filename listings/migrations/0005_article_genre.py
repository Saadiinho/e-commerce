# Generated by Django 3.2.20 on 2023-07-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_article_isnew'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='genre',
            field=models.CharField(choices=[('Bur', 'Bureau'), ('Cui', 'Cuisine'), ('Sdb', 'Salle De Bain'), ('Sal', 'Salon'), ('Cha', 'Chambre')], default='', max_length=10),
            preserve_default=False,
        ),
    ]