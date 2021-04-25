from django.shortcuts import render
import os
from subprocess import *
from django import forms

inicio = True
dondestoy= "/raiz"

def home(request):
    ubicacion= getoutput("pwd")
    return render(request, "index.html",{"ubicacion": ubicacion})

def crear(request):
    ubi(dondestoy)
    try:
        tipo= request.GET["tipo"]
        nombre= request.GET["nombre"]
        if tipo == "carpeta":
            os.system(f"mkdir {nombre}")
            aviso="La carpeta ha sido creada."
        else:
            os.system(f"touch {nombre}")
            aviso="La carpeta ha sido creada."
    except:
        aviso=""

    ubicacion= getoutput("pwd")
    return render(request,"Crear.html",{"ubicacion":ubicacion,"aviso":aviso})

def borrar(request):
    ubi(dondestoy)
    try:
        nombre= request.GET["nombre"]
        os.system(f"rm -r {nombre}")
        aviso="Ha sido elimida con exito."
    except:
        aviso=""

    ubicacion= getoutput("pwd")
    return render(request,"Borrar.html",{"ubicacion":ubicacion,"aviso":aviso})

def copiar(request):
    return render(request,"copiar.html")

def renombrar(request):
    return render(request,"Renombrar.html")

def mover(request):
    return render(request,"Mover.html")

def verPermisos(request):
    return render(request,"VerPermisos.html")

def cambiarPermisos(request):
    ubi(dondestoy)
    try:
        tipo = request.POST["tipo"]
        permisos= request.POST["permisos"]
        nombre= request.POST["nombre"]
        if tipo == "carpeta":
            so.system(f"sudo chmod {permisos} -R {nombre}")
        else:
            so.system(f"sudo chmod {permisos} {nombre}")

        aviso="Se han cambiado los permisos con exito"
    except:
        aviso="Hay una falla"

    ubicacion= getoutput("pwd")
    return render(request,"CambiarPermisos.html",{"ubicacion":ubicacion,"aviso": aviso})

def cambiarPropietario(request):
    return render(request,"CambiarPropietario.html")


def ubi(carpetaName):
    try:
        os.chdir(getoutput("pwd")+carpetaName)
    except:
        mensaje="No existe el directorio"

def abrir(request):
    try:
        nombre=request.GET['carpeta']
        global dondestoy
        dondestoy= dondestoy+"/"+nombre
        ubi(dondeestoy)
    except:
        mensaje="Carpeta prohibida"
    ubicacion= getoutput("pwd")
    #codigo de mostrar carpetas
    return render(render,"index.html", {"ubicacion":ubicacion})