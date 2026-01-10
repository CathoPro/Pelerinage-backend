from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('inscription/', views.inscription, name="inscription"),
    path('paiement/', views.paiement, name="paiement"),
    path('recu/<int:id>/', views.recu, name="recu"),
    path('felicitation/', views.felicitation, name="felicitation"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('boutique/', views.boutique, name="boutique"),
]
