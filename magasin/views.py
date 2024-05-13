from django.shortcuts import render , redirect
from django.template import loader
from .models import Produit
from .models import Fournisseur
from .models import Commande
from .forms import ProduitForm
from .forms import FournisseurForm
from .forms import CommandeForm
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer , ProduitSerializer
from django.contrib.auth import logout

@login_required
def indexed(request):
    context={'val':"Menu Acceuil"}
    return render(request,'magasin/acceuil.html',context)
def index(request):
    products= Produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html ',context )

def index2(request):
 if request.method == "POST" :
  form = ProduitForm(request.POST,request.FILES)
  if form.is_valid():
    form.save()
  return redirect('/magasin')
 else :
   form = ProduitForm() #créer formulaire vide
 return render(request,'magasin/majProduits.html',{'form':form})
def index1(request):
  list=Produit.objects.all()
  return render(request,'magasin/vitrine.html',{'list':list})
def nouveauFournisseur(request):
  if request.method == 'POST':
    form = FournisseurForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FournisseurForm()
  fournisseurs=Fournisseur.objects.all()
  context={'form': form,'fournisseurs':fournisseurs}
  return render(request,'magasin/fournisseur.html',context)

def indexC(request):
  if request.method == 'POST':
    form = CommandeForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = CommandeForm()
  commandes=Commande.objects.all()
  context={'form': form,'commandes':commandes}
  return render(request,'magasin/commande.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('magasin/accueil/')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
def logout_view(request): 
  logout(request)
  return redirect('login')
class CategoryAPIView(APIView):
 def get(self, *args, **kwargs):
  categories = Categorie.objects.all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)
 
class ProduitAPIView(APIView):
 def get(self, *args, **kwargs):
  produit = Produit.objects.all()
  serializer = ProduitSerializer(produit, many=True)
  return Response(serializer.data)
 
from rest_framework import viewsets
class ProductViewset(viewsets.ReadOnlyModelViewSet):
  serializer_class = ProduitSerializer
  def get_queryset(self):
    queryset = Produit.objects.filter()
    category_id = self.request.GET.get('category_id')
    if category_id:
      queryset = queryset.filter(categorie_id=category_id)
    return queryset