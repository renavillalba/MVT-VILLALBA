from django.shortcuts import render
from Familiares.models import Familiar
from django.http import HttpResponse
from django.template import loader

def intro_message(request):

    mensaje_inicial = "Informacion de familiares"
    dicc = {"mensaje" : mensaje_inicial}
    plantilla_inicial = loader.get_template("plantilla_1.html")
    mostrar_mensaje = plantilla_inicial.render(dicc)

    return HttpResponse(mostrar_mensaje)

def fecha_nacimiento(request, edad):

    anio_nacimiento = 2022 - int(edad)

    return anio_nacimiento

'''def integrantes(request, nacimiento):

    fecha = fecha_nacimiento(nacimiento) 

    integrante_1 = Familiar(nombre = "Santiago", estatura = 1.78, fecha_de_nacimiento = fecha_nacimiento)
    integrante_2 = Familiar(nombre = "Emilia", estatura = 1.60, fecha_de_nacimiento = fecha_nacimiento)
    integrante_3 = Familiar(nombre = "Susana", estatura = 1.62, fecha_de_nacimiento = )
    integrante_4 = Familiar(nombre = "Gaston", estatura = 1.70, fecha_de_nacimiento = "")

    return HttpResponse()'''