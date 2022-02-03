from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    tag = models.ManyToManyField('Tag')
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.image.url