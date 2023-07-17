# Generated by Django 3.2.20 on 2023-07-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_alter_article_dimension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dimension',
            field=models.CharField(choices=[('XS', 'Xs'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'Xl')], max_length=3),
        ),
    ]