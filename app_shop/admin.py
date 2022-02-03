from django.contrib import admin
from .models import Product, Tag, ImageGallery

class ImageGalleryInline(admin.StackedInline):
    model = ImageGallery
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(ImageGallery)