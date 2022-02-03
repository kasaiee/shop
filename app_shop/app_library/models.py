from distutils.command.upload import upload
from unicodedata import name
from django.db import models
from django.forms import CharField

# Create your models here.
class Book(models.Model):
    name = models.CharField(null = True, max_length=150)
    cover = models.ImageField(upload_to='cover', null=True)
    price = models.PositiveIntegerField(null=True)
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.name