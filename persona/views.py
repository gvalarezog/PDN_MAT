from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from persona.forms import PersonaFormulario
from persona.models import Persona


def detalle_persona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    mensaje = {'persona':persona}
    return render(request, 'detalle.html', mensaje)

#PersonaFormulario = modelform_factory(Persona, exclude=[])
def nueva_persona(request):
    if request.POST:
        formPersona = PersonaFormulario(request.POST)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('inicio')
    else:
        formPersona = PersonaFormulario()
    return render(request, 'nueva.html', {'formPersona': formPersona})


def modificar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formPersona = PersonaFormulario(request.POST, instance=persona)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('inicio')
    else:
        formPersona = PersonaFormulario(instance=persona)
    mensaje = {'formPersona': formPersona}
    return render(request, 'modificar.html', context=mensaje)


def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')
