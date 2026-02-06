from django.contrib import admin
from .models import Maktab, Oquvchi, Oqituvchi, Gurux

# Register your models here.




@admin.register(Maktab)
class MaktabAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'direktor', 'ishga_tushurilgan_vaqt')
    search_fields = ('nom',)


@admin.register(Oquvchi)
class OquvchiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'familya', 'maktab')
    list_filter = ('maktab',)


@admin.register(Oqituvchi)
class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'familya', 'maktab')
    list_filter = ('maktab',)


@admin.register(Gurux)
class GuruxAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'ustoz', 'dars_vaqti')
    filter_horizontal = ('oquvchilar',)
