from django.db import models
from video_encoding.fields import VideoField
from tinymce.models import HTMLField

class Explication(models.Model):
    titre = models.CharField(max_length=200)
    contenu = HTMLField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='statu.jpg')

    def __str__(self):
        return self.titre


class Video(models.Model):
    fichier = VideoField(upload_to="video/", null=True, blank=True) 
    explication = models.ForeignKey(Explication, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return f"{self.explication}"

        

class Commentaire(models.Model):
    auteur = models.CharField(max_length=255, default="Anonyme")
    explication = models.ForeignKey(Explication, on_delete=models.CASCADE, related_name='commentaires')
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.explication} {self.date_publication}"
