from django.contrib import admin
from .models import Nature, AccessoireHistorique, Accessoire, BatterieHistorique, Batterie, Client, Pneu, PneuHistorique, Fournisseur, Historique, Administrateur, Marque, Numero, Transaction

# Register your models here.

# admin.site.register(Pneu) 4
admin.site.register(PneuHistorique)
# admin.site.register(Fournisseur) 3
# admin.site.register(Historique) 6
# admin.site.register(Client) 5
admin.site.register(Administrateur)
# admin.site.register(Marque) 1
# admin.site.register(Numero) 2
# admin.site.register(Transaction) 7
admin.site.register(Nature)
# admin.site.register(Accessoire) 9
admin.site.register(AccessoireHistorique)
admin.site.register(BatterieHistorique)
# admin.site.register(Batterie) 8

class NumeroAdmin(admin.ModelAdmin):
    search_fields = ['Numero']

admin.site.register(Numero, NumeroAdmin)

class MarqueAdmin(admin.ModelAdmin):
    search_fields = ['Nom']

admin.site.register(Marque, MarqueAdmin)

class FournisseurAdmin(admin.ModelAdmin):
    search_fields = ['Nom', 'Contact']

admin.site.register(Fournisseur, FournisseurAdmin)

class PneuAdmin(admin.ModelAdmin):
    search_fields = ['Details', 'Stockage', 'Numero__Numero', 'Marque__Nom', 'Fournisseur__Nom']

admin.site.register(Pneu, PneuAdmin)

class ClientAdmin(admin.ModelAdmin):
    search_fields = ['Nom', 'Contact']

admin.site.register(Client, ClientAdmin)

class HistoriqueAdmin(admin.ModelAdmin):
    search_fields = ['Designation', 'Client__Nom']

admin.site.register(Historique, HistoriqueAdmin)

class TransactionAdmin(admin.ModelAdmin):
    search_fields = ['Details', 'Stockage', 'Numero__Numero', 'Marque__Nom', 'Fournisseur__Nom', 'Nature__Name']

admin.site.register(Transaction, TransactionAdmin)

class BatterieAdmin(admin.ModelAdmin):
    search_fields = ['Details', 'Stockage', 'Numero__Numero', 'Marque__Nom', 'Fournisseur__Nom']

admin.site.register(Batterie, BatterieAdmin)

class AccessoireAdmin(admin.ModelAdmin):
    search_fields = ['Details', 'Stockage', 'Numero__Numero', 'Marque__Nom', 'Fournisseur__Nom']

admin.site.register(Accessoire, AccessoireAdmin)