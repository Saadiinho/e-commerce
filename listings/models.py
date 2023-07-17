from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Article(models.Model):
    class Genre(models.TextChoices):
        Bureau = 'Bur'
        Cuisine = 'Cui'
        Salle_de_bain = 'Sdb'
        Salon = 'Sal'
        Chambre = 'Cha'
        Decoration = 'Dec'
    class Dimension(models.TextChoices):
        XS = 'XS'
        S ='S'
        M = 'M'
        L = 'L'
        XL = 'XL'
    name = models.fields.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    dimension = models.CharField(choices=Dimension.choices, max_length=3)
    bigDescription = models.CharField(max_length=2000)
    isOnTrend = models.BooleanField(default=False)
    isNew = models.BooleanField(default=False)
    genre = models.fields.CharField(choices=Genre.choices, max_length=10)
    image = models.ImageField(upload_to='images')
    available = models.fields.BooleanField(default=True)
    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.article}'

class SocialNetwork(models.Model):
    name = models.fields.CharField(max_length=50)
    url = models.URLField()
    logo = models.fields.CharField(max_length=2000)
    def __str__(self):
        return f'{self.name}'