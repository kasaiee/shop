from django.contrib import admin
from .models import Book
from django.utils.safestring import mark_safe
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'price', 'pub_date', 'get_cover')
    list_editable = ('price', 'pub_date')
    list_filter = ('pub_date',)
    def get_cover(self, obj):
        return mark_safe(f'<img style ="width: 100px" src ="{obj.cover.url}" />')


admin.site.register(Book, BookAdmin)