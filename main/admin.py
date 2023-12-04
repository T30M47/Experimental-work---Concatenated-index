from django.contrib import admin
from .models import *
# Register your models here.
modeli = [Proizvod_SIndeksom, Proizvod_bezIndeksa, Proizvod_DioIndeksa, Proizvod_KriviIndeks]

admin.site.register(modeli)