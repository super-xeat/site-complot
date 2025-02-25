from django.contrib import admin
from .models import Theorie, Commentaire, Video

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 1

class TheorieAdmin(admin.ModelAdmin):
    inlines = [VideoInline, CommentaireInline]


admin.site.register(Theorie, TheorieAdmin)
admin.site.register(Commentaire)
