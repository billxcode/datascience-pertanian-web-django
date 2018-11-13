from django.contrib import admin

from .models import Kriteria, Bobot, Tanaman, NameKriteria

# Register your models here.

admin.site.register(Tanaman)
admin.site.register(Kriteria)
admin.site.register(Bobot)
admin.site.register(NameKriteria)