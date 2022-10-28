from fcntl import DN_DELETE
from django.db import models
# Create your models here.

class Artiste(models.Model):
     first_name = models.CharField(_MAX_LENGTH=40)
     last_name = models.CharField(_MAX_LENGTH=40)
     age = models.IntegerField(_MAX_LENGTH=200)

class Song(models.Model):
     Artiste = models.ForeignKey(Artiste, DN_DELETE-models.CASCADE)
     title = models.CharField(_MAX_LENGTH=40)
     date_released = models.DateField(_MAX_LENGTH=40)
     likes = models.CharField(_MAX_LENGTH=400)
     artiste_id = models.CharField(_MAX_LENGTH=40)

class lyric(models.model):
     content = models.CharField(_MAX_LENGTH=400)
     song_id = models.CharField(_MAX_LENGTH=400)
