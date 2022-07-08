from django.forms import ModelForm, EmailInput

from persona.models import Persona


class PersonaFormulario(ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'email','telefono')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }