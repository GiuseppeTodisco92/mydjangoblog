from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model) :
    titolo = models.CharField(max_length=120)
    contenuto = models.TextField()
    #auto_now add viene settato solo quando viene creato ecco perchè viene settato True
    data = models.DateField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

# questa funzione ci permette di mostrare il titolo all interno della sezione post admin
    def __str__(self):
        return self.titolo

    #best practice per ottenere l 'url di un post singolo 
    def get_absolute_url(self):
        return reverse("singolo", kwargs = {"id": self.id, "slug": self.slug})
