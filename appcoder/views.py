from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Familia


# Create your views here.

def datosfamilia(request):
    familiar = Familia.objects.all()
    dicc = {'familiar': familiar}
    
    
    familiar1 = Familia(nombre = 'Carlos Pérez', dni = 29750120, fecha = "1985-4-14", ciudad = "Corrientes", email = "fanadeallboys@gmail.com")
    familiar1.save()
    familiar2 = Familia(nombre = 'Juan Giménez', dni = 19550220, fecha = "1981-2-26", ciudad = "Buenos Aires", email = "amigodepepinrodriguez@gmail.com")
    familiar2.save()
    familiar3 = Familia(nombre = 'Pablo Rodríguez', dni = 33120337, fecha = "1921-9-12", ciudad = "Mar del Plata", email = "elviejodelaexpoarmas@gmail.com")
    familiar3.save()
    familiar4 = Familia(nombre = 'Bernardo de Irigoyen', dni = 1550220, fecha = "1902-8-12", ciudad = "Capital Federal", email = "laucrnohamuerto@gmail.com")
    familiar4.save()

    template = loader.get_template("familiadatos.html")
    documento = template.render(dicc)
    return HttpResponse(documento)


    

