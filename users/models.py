from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    avatar = models.ImageField(upload_to="avatar/",default="default_avatar.jpg", null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profil de {self.username}"