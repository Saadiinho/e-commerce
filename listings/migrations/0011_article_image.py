# Generated by Django 3.2.20 on 2023-07-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
