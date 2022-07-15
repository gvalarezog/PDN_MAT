"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from persona.views import detalle_persona, nueva_persona, modificar_persona, eliminar_persona,reporte_personas
from webapp.views import bienvenidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos, name='inicio'),
    path('detalle_persona/<int:id>', detalle_persona, name='detalle_persona'),
    path('nueva_persona/', nueva_persona, name='nueva_persona'),
    path('modificar_persona/<int:id>', modificar_persona, name='modificar_persona'),
    path('eliminar_persona/<int:id>', eliminar_persona, name='eliminar_persona'),
    path('reporte_personas/', reporte_personas, name='reporte_personas'),
]
