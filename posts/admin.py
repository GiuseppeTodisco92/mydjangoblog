from django.contrib import admin

# Register your models here.
# dal file models importa post - in questa maniera sarà visualizzato nella sezione admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    #__str__ è la funzione che restituisce il titolo in models
    list_display = ["__str__","data"]
    # list_filter ci permette di filtrare i dati in questo caso in base alla data 
    list_filter = ["data"]
    # search_fields serve per geneare un campo di ricerca per titolo e contenuto 
    search_fields = ["titolo", "contenuto"]
    #il prepopulated_fields serve per far matchare allo slug il titolo 
    prepopulated_fields = {"slug": ("titolo",)}

    #questa classe chiamata meta fornisce al nostro postadmin informazioni sul modello che sta utilizzando 
    class Meta:
        model = Post

#per registrare il modello post nella sezione autorizazzione  E ANCHE PostAdmin
admin.site.register(Post, PostAdmin)

