from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("sortie", views.sortie, name="sortie"),
    path("entre", views.entre, name="entre"),
    path("achat/<int:client_id>", views.achat, name="achat"),
    path("historique/<int:client_id>/", views.historique, name="historique"),
    path("listclient", views.list_client, name="list_client"),
    path("credit", views.credit, name="credit"),
    path("stock", views.stock, name="stock"),
    # path("", views.connexion, name="connexion"),
    path("", views.PageConnexion, name="PageConnexion"),
    path("get_marques", views.get_marques, name="get_marques"),
    path("get_natures", views.get_natures, name="get_natures"),
    path("get_numeros", views.get_numeros, name="get_numeros"),
    path("listfournisseur", views.list_fournisseur, name="list_fournisseur"),
    path("transaction", views.transaction, name="transaction"),
    path('logout', views.logout, name="logout")
]