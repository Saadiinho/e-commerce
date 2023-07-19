from django.contrib import admin
from listings.models import Article, Review, SocialNetwork, Cart, CartItem
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'isNew', 'isOnTrend', 'genre')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Review)
admin.site.register(SocialNetwork)
admin.site.register(Cart)
admin.site.register(CartItem)