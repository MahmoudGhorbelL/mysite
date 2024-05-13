from django.db import models
from datetime import date

# Create your models here.

class Produit(models.Model):
    TYPE_CHOICES = [('fr','From'),('cs','Conserve'),('em','emballé')]
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.000)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES , default='em')
    img = models.ImageField(blank=True)
    categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True )
    fournisseur = models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True )
    def __str__(self) -> str:
        return "description" +str(self.description)+" "+"prix:" +str(self.prix)+" "+"type : "+str(self.type) + " "+ "Categorie"+str(self.categorie)+ " "+ "Fournisseur"+str(self.fournisseur)
    
#class Fournisseur(models.Model):
class Categorie(models.Model):
    TYPE_CHOICES =[('Al','Alimentaire') , ('Mb','Meuble'),('Sn','Sanitaire'), ('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name = models.CharField(max_length=50,choices=TYPE_CHOICES,default='Alimentaire')
    def __str__(self) -> str:
        return "name" +str(self.name) 
class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)   
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    def __str__(self) -> str:
        return "Nom: " +str(self.nom)+" "+"adresse :" +str(self.adresse)+" "+"Email : "+str(self.email) + " "+ "Telephone"+str(self.telephone)
class ProduitNC(Produit,models.Model):
    Duree_garantie =models.CharField (max_length=100)
    def __str__(self) -> str:
        return super().__str__() + " " + str(self.Duree_garantie)
    
class Commande(models.Model):
    dateCde = models.DateField(null=True,default=date.today)
    totalCde = models.DecimalField(max_digits=10,decimal_places=3)
    produits = models.ManyToManyField(Produit)
    
    def calculPrix(self):
        total = 0
        for produit in self.produits.all():
            total += produit.prix
        return total
    def string(self):
        ch = ""
        for p in self.produits.all():
            ch = ch + str(p) + " "
        return ch
    def __str__(self):
        return f"{self.dateCde} {self.totalCde} {self.calculPrix()} {self.string()}" 
    
