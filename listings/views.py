from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator
from listings.models import Article, Review, SocialNetwork
from listings.form import ReviewForm, ContactUsForm


# Create your views here.
def accueil(request):
    articles = Article.objects.all()
    return render(request, 'listings/index.html', {'articles': articles})

def boutique(request):
    articles = Article.objects.all()

    if request.method == 'POST':
        # Filtrage par prix
        filter_price = request.POST.get('selectPrice')
        if filter_price == '1':
            articles_price = Article.objects.filter(Q(price__gt=0.0) & Q(price__lte=99.99))
        elif filter_price == '2':
            articles_price = Article.objects.filter(Q(price__gte=100.0) & Q(price__lte=199.99))
        elif filter_price == '3':
            articles_price = Article.objects.filter(Q(price__gte=200.0))
        else:
            articles_price = articles

        # Filtrage par catégorie
        filter_category = request.POST.get('selectCategory')
        if filter_category == '1':
            articles_category = Article.objects.filter(genre='Sal')
        elif filter_category == '2':
            articles_category = Article.objects.filter(genre='Cui')
        elif filter_category == '3':
            articles_category = Article.objects.filter(genre='Sdb')
        elif filter_category == '4':
            articles_category = Article.objects.filter(genre='Bur')
        elif filter_category == '5':
            articles_category = Article.objects.filter(genre='Cha')
        elif filter_category == '6':
            articles_category = Article.objects.filter(genre='Dec')
        else:
            articles_category = articles

        #Filtrage par dimension
        filter_dimension = request.POST.get('selectDimension')
        if filter_dimension == '1':
            articles_dimension = Article.objects.filter(dimension='XS')
        elif filter_dimension == '2':
            articles_dimension = Article.objects.filter(dimension='S')
        elif filter_dimension == '3':
            articles_dimension = Article.objects.filter(dimension='M')
        elif filter_dimension == '4':
            articles_dimension = Article.objects.filter(dimension='L')
        elif filter_dimension == '5':
            articles_dimension = Article.objects.filter(dimension='XL')
        else:
            articles_dimension = articles

        # Filtrage par disponibilité
        filter_available = request.POST.get('selectAvailable')
        if filter_available == '1':
            articles_available = Article.objects.filter(available=True)
        elif filter_available == '2':
            articles_available = Article.objects.filter(available=False)
        else:
            articles_available = articles

        # Concaténation des résultats des filtres
        articles = articles_price & articles_category & articles_dimension & articles_available

    if request.method == 'GET':
        name = request.GET.get('recherche')
        if name is not None:
            articles = Article.objects.filter(name__icontains=name)
    paginator = Paginator(articles, 12)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'listings/boutique.html', {'articles': articles})

def article_detail(request, id):
    articles = Article.objects.get(id=id)
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST, initial={'article': articles})
        if form.is_valid():
            review = form.save()
        return redirect('boutique')
    else: 
        form = ReviewForm()
    return render(request,'listings/article_detail.html', {'articles': articles, 'reviews': reviews, 'form': form})

def panier(request):
    articles = Article.objects.all()
    return render(request, 'listings/panier.html', {'articles': articles})

def contact(request):
    socials = SocialNetwork.objects.all()
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lasttName = request.POST.get('firstName')
        mail = request.POST.get('email')
        messagePoste = request.POST.get('message')
        send_mail(
            subject=f'Message de la boutique ',
            message=messagePoste,
            from_email=mail,
            recipient_list=['saad.rafiqul1@gmail.com'],
        )
    return render(request, 'listings/contact.html', {'socials': socials})