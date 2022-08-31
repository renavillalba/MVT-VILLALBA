from django.shortcuts import render
from Familiares.models import Familiar
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def intro_message(request):

    mensaje_inicial = "Informacion de familiares"
    dicc = {"mensaje" : mensaje_inicial}
    plantilla_inicial = loader.get_template("plantilla_1.html")
    mostrar_mensaje = plantilla_inicial.render(dicc)

    return HttpResponse(mostrar_mensaje)

def integrantes(request):

    integrante_1 = Familiar(nombre = "Santiago", estatura = 1.78, fecha_de_nacimiento = datetime.date(1972, 4, 24))
    integrante_2 = Familiar(nombre = "Emilia", estatura = 1.60, fecha_de_nacimiento = datetime.date(2004, 12, 18))
    integrante_3 = Familiar(nombre = "Susana", estatura = 1.62, fecha_de_nacimiento = datetime.date(1996, 8, 22))
    integrante_4 = Familiar(nombre = "Gaston", estatura = 1.70, fecha_de_nacimiento = datetime.date(1980, 3, 8))

    integrante_1.save()
    integrante_2.save()
    integrante_3.save()
    integrante_4.save()
    
    dicc_familia = {"Miembro_1" : integrante_1, "Miembro_2" : integrante_2, "Miembro_3" : integrante_3, "Miembro_4" : integrante_4}
    
    return render(request, "plantilla_1.html", dicc_familia)