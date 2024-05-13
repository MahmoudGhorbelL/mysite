from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.forms import PostForm
from .models import Post
class ListePostes(ListView):
    model = Post
    template_name = 'blog/liste_Postes.html'
    context_object_name = 'postes'
class DetailPoste(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'post'
class CreerPoste(CreateView):
    model = Post
    template_name = 'blog/creer_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_postes') 
class ModifierPoste(UpdateView):
    model = Post
    template_name = 'blog/modifier_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_postes')
class SupprimerPoste(DeleteView):
    model = Post
    template_name = 'blog/supprimer_post.html'
    success_url = reverse_lazy('liste_postes') 