# Generated by Django 5.1.6 on 2025-02-20 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debunk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='auteur',
            field=models.CharField(default='Anonyme', max_length=255),
        ),
    ]
