# Generated by Django 5.1.6 on 2025-03-05 18:00

import tinymce.models
import video_encoding.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', tinymce.models.HTMLField(default='Contenu par défaut')),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='statu.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', video_encoding.fields.VideoField(blank=True, null=True, upload_to='video/')),
            ],
        ),
    ]
