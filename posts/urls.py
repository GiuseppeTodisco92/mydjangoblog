
from django.urls import path
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post
#lista dei post | homepage del blog
# post singoli del blog
# sezione contatti 

urlpatterns = [
    path('', ListView.as_view(
        #stiamo prendendo tutti i post dal database
        queryset = Post.objects.all().order_by("-data"), #ordiniamo per data negativa cioè gli ultimi scritti
        template_name = "lista_post.html"), name = "lista"),
        #generata questa funzione è una sorta di scorciatoia per la quale possiasmo eliminare dal file views.py il def lista_post
        #il compito del list view è quello di mostrarci il contenuto del database in lista
    
    path('<int:id>/<slug:slug>/', DetailView.as_view(
        model = Post,
        template_name = "post_singolo.html"), name = "singolo"),
    path('contatti/', posts_views.contatti, name = "contatti"),
    
]
