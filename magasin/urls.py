from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import CategoryAPIView , ProduitAPIView , ProductViewset

urlpatterns = [
    path('ecomerce/', views.index2 , name='ecomerce'),
    path('vitrine/', views.index1, name='vitrine'),
    path('', views.index, name='index'),
    path('accueil/', views.indexed, name='indexed'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
    path('nouvCommande/',views.indexC,name='nouveauCom'),
    path('register/',views.register, name = 'register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)