from django.contrib import admin

from .models import Kriteria, Bobot, Tanaman, NameKriteria, NameArea, RatioQuality

# Register your models here.

class TanamanAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_area', 'pub_date')

class KriteriaAdmin(admin.ModelAdmin):
    list_display = ('tanaman', 'value', 'name_kriteria', 'periode', 'pub_date')

class BobotAdmin(admin.ModelAdmin):
    list_display = ('name_kriteria', 'value')

class NameKriteriaAdmin(admin.ModelAdmin):
    list_display = ('name')

class NameAreaAdmin(admin.ModelAdmin):
    list_display = ('name')

class RatioQualityAdmin(admin.ModelAdmin):
    list_display = ('tanaman', 'value')

admin.site.register(Tanaman, TanamanAdmin)
admin.site.register(Kriteria, KriteriaAdmin)
admin.site.register(Bobot, BobotAdmin)
admin.site.register(NameKriteria)
admin.site.register(NameArea)
admin.site.register(RatioQuality, RatioQualityAdmin)