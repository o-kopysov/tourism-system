from django.conf import settings
from django.db import models
from django.shortcuts import reverse

class Sight(models.Model):
    name_sight = models.CharField(max_length=60)
    description = models.TextField()
    img = models.ImageField(upload_to='photo_sight')
    year = models.IntegerField()
    address = models.CharField(max_length=100)
    link = models.URLField()
    slug = models.SlugField()

    

    def get_absolute_url(self):
        return reverse("sight", kwargs = {
        'slug': self.slug
        })
