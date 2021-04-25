from django.shortcuts import render
import os
from subprocess import *
from django import forms

inicio = True
principalub= ""

def home(request):
    ubicacion= getoutput("pwd")
    return render(request, "index.html",{"ubicacion": ubicacion})

def crear(request):
    try:
        os.chdir(getoutput("pwd")+"/raiz")
    except:
        mensaje="quetal"

    try:
        tipo= request.GET["tipo"]
        if tipo == "carpeta":
            nombre= request.GET["nombre"]
            os.system(f"mkdir {nombre}")
            mensaje="holi"
        else:
            os.system(f"touch {nombre}")
    except:
        mensaje="problemas"


    ubicacion= getoutput("pwd")
    return render(request,"Crear.html",{"ubicacion":ubicacion,"mensaje":mensaje})

def borrar(request):
    return render(request,"Borrar.html")

def copiar(request):
    return render(request,"copiar.html")

def renombrar(request):
    return render(request,"Renombrar.html")

def mover(request):
    return render(request,"Mover.html")

def verPermisos(request):
    return render(request,"VerPermisos.html")

def cambiarPermisos(request):
    return render(request,"CambiarPermisos.html")

def cambiarPropietario(request):
    return render(request,"CambiarPropietario.html")

