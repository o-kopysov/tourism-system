from django.db import models

class Sight(models.Model):
    name_sight = models.CharField(max_length=60)
    description = models.TextField()
    img = models.ImageField(upload_to='photo_sight')
    year = models.IntegerField()
    address = models.CharField(max_length=100)
    link = models.URLField()
    
