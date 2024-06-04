from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
import random
from inicio.models import Auto

def inicio(request):
    return render(request,'inicio/index.html')
    # return HttpResponse('Bienvenido a mi inicio!!')

def template1(request,nombre,apellido, edad):
    fecha = datetime.now()
    suma = 4 + edad
    return HttpResponse(f'<h1>Mi template 1 </h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido} {edad}')

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r'C:\Users\GiovanniFranciscoPer\Desktop\Curso\proyecto\templates\template2.html')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    fecha = datetime.now()
    
    datos = {'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
        }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def template3(request, nombre, apellido, edad):
    
    template = loader.get_template('template2.html')
    
    fecha = datetime.now()
    
    datos = {'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
        }
      
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)

def template4(request, nombre, apellido, edad):
    
    fecha = datetime.now()
    
    datos = {'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
        }
    
    return render(request, 'template2.html',datos)

def probando(request):
    lista = list(range(500))
    numeros = random.choices(lista,k=50)
    
    return render(request, 'probando_if_for.html', {'numeros' : numeros})

def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca,modelo=modelo)
    auto.save()
    return render(request, 'auto_templates/creacion.html',{'auto':auto})