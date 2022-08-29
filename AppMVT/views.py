from django.template import Template,Context
from django.http import HttpResponse
from .models import *
from django.template import loader
import datetime
from Plantillas import *

# Create your views here.

def familia(request):
    familiar1=Familia(DNI=37497802,nombre="Fernando",parentezco="Hijo",fecha_de_cumpleaños=1993/10/14)
    #familiar2=Familia(DNI=14567687,nombre="Virginia",paretezco="Madre",fecha_de_cumpleaños=1963/12/4)
    #familiar3=Familia(DNI=39456987,nombre="Agustina",paretezco="Hija",fecha_de_cumpleaños=1995/9/25)
    familiar1.save()
    #familiar2.save()
    #familiar3.save()
    fliar1=f"DNI: {familiar1.DNI} Nombre: {familiar1.nombre} Parentezco: {familiar1.parentezco} Cumpleaños: {familiar1.fecha_de_cumpleaños}"
    #fliar2=f"DNI: {familiar2.DNI} Nombre: {familiar2.nombre} Parentezco: {familiar2.paretezco} Cumpleaños: {familiar2.fecha_de_cumpleaños}"
    #fliar3=f"DNI: {familiar3.DNI} Nombre: {familiar3.nombre} Parentezco: {familiar3.paretezco} Cumpleaños: {familiar3.fecha_de_cumpleaños}"
    return HttpResponse(fliar1)#,fliar2,fliar3)

def TemplateMVT(request):
    Ruta=open("C:/Users/fvaca/OneDrive - SA San Miguel A.G.I.C.I. y F/Escritorio/Fer/Otros/Cursos/Python/CH/Clase 17 - 18/MVT-Entregable/MVTFernandoVaca II/Plantillas/TemplateMVT.html")
    plantilla=Template(Ruta.read())
    Ruta.close()
    Contexto=Context()
    Documento=plantilla.render(Contexto)
    return HttpResponse(Documento)




