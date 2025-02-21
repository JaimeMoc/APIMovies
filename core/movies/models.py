from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField( max_length = 255, unique = True)
    year = models.IntegerField()
    synopsis = models.TextField( null = True, blank = True) 

    def __str__(self):
        return self.name
