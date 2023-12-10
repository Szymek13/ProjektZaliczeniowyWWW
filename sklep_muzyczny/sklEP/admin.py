from django.contrib import admin

# Register your models here.

from .models import Producent
from .models import Album
from .models import Wytwornia
from .models import Festiwal
from .models import Gatunek

class ProducentAdmin(admin.ModelAdmin):
    list_display = ['pseudonim', 'imie', 'nazwisko', 'pochodzenie']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'autor', 'rodzaj', 'gatunek', 'data_premiery', 'ilosc_utworow']

class FestiwalAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']

class WytworniaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'zalozyciel', 'siedziba']

admin.site.register(Producent, ProducentAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Wytwornia, WytworniaAdmin)
admin.site.register(Festiwal, FestiwalAdmin)
admin.site.register(Gatunek)
