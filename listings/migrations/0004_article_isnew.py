# Generated by Django 3.2.20 on 2023-07-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_article_isontrend'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isNew',
            field=models.BooleanField(default=False),
        ),
    ]
