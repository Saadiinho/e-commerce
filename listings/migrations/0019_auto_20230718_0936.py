# Generated by Django 3.2.20 on 2023-07-18 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_panier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.article')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.cart')),
            ],
        ),
        migrations.DeleteModel(
            name='Panier',
        ),
    ]