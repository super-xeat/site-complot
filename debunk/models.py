from django.db import models
from video_encoding.fields import VideoField
from tinymce.models import HTMLField
from django.conf import settings



class Explication(models.Model):
    titre = models.CharField(max_length=200)
    contenu = HTMLField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='statu.jpg')

    def __str__(self):
        return self.titre


class Video(models.Model):
    fichier = VideoField(upload_to="video/", null=True, blank=True) 
    explication = models.ForeignKey(Explication, on_delete=models.CASCADE, related_name='videos', null=True, blank=True)

    def __str__(self):
        return f"{self.explication}"

        

class Commentaire(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='commentaires_debunk')
    explication = models.ForeignKey(Explication, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auteur.username} {self.explication}"
