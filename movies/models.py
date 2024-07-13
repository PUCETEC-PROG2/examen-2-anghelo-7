from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=30, null=False)
    direction = models.CharField(max_length=30, null=False)
    year_publication = models.IntegerField(null = False)
    synopsis = models.TextField(max_length=200, null=False)
    
    def __str__(self) -> str:
        return self.title