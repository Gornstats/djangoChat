from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return self.name
