# Generated by Django 3.2.20 on 2023-07-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_article_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ManyToManyField(to='listings.Article')),
            ],
        ),
    ]
