from django.contrib import admin

# Register your models here.
from cms.models import Menu, PaginaHome, Configuracion


admin.site.register(Menu)
admin.site.register(Configuracion)
admin.site.register(PaginaHome)
