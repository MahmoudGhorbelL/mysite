from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListePostes, DetailPoste, CreerPoste, ModifierPoste, SupprimerPoste

urlpatterns = [
    path('', ListePostes.as_view(), name='liste_postes'), 
    path('<int:pk>/', DetailPoste.as_view(), name='detail_poste'),
    path('ajouter/', CreerPoste.as_view(), name='creer_poste'),
    path('<int:pk>/modifier/', ModifierPoste.as_view(), name='modifier_poste'),
    path('<int:pk>/supprimer/', SupprimerPoste.as_view(), name='supprimer_poste'),
]
