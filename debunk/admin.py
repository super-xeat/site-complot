from django.contrib import admin
from .models import Explication, Commentaire, Video

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 1

class ExplicationAdmin(admin.ModelAdmin):
    inlines = [VideoInline, CommentaireInline]


admin.site.register(Explication, ExplicationAdmin)
admin.site.register(Commentaire)

