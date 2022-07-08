from django.contrib import admin

# Register your models here.
from persona.models import Persona, Telefono, Direccion

admin.site.register(Persona)
admin.site.register(Telefono)
admin.site.register(Direccion)
