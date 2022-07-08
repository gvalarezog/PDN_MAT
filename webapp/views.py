from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from persona.models import Persona


def bienvenidos(request):
    cantidad = Persona.objects.count()
    # personas = Persona.objects.all().values()
    personas = Persona.objects.order_by('apellido')
    mensaje = {'cantidad':cantidad, 'personas':personas}
    pagina = loader.get_template('bienvenidos.html')
    return HttpResponse(pagina.render(mensaje, request))
