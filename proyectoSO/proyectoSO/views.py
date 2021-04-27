from django.shortcuts import render
import os
from subprocess import *
from django import forms

inicio = True
dondestoy= "/raiz"

def home(request):
    #ubi(dondestoy)
    ubicacion= getoutput("pwd")
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request, "index.html",{"ubicacion": ubicacion, "archivos2": iconos1, "carpetas2": iconos2})

def mostrar_archivos():
    archivos = getoutput("find . -maxdepth 1 -type f")
    archivos = archivos.split("\n")
    archivos2 = []
    for i in range(len(archivos)):
        archivos2.append(archivos[i][2:])
    return archivos2

def mostrar_carpetas():
    carpetas = getoutput("find . -maxdepth 1 -type d")
    carpetas = carpetas.split("\n")
    carpetas2 = []
    for i in range(len(carpetas)):
        if (carpetas[i][2:] != ""):
            carpetas2.append(carpetas[i][2:])
    return carpetas2

def crear(request):
    #ubi(dondestoy)
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
    #ubi(dondestoy)
    try:
        nombre= request.GET["nombre"]
        os.system(f"rm -r {nombre}")
        aviso="Ha sido elimida con exito."
    except:
        aviso=""

    ubicacion= getoutput("pwd")
    return render(request,"Borrar.html",{"ubicacion":ubicacion,"aviso":aviso})

def copiar(request):
    
    try:
      tipo= request.GET["tipo"]
      archivo= request.GET["ubA"]
      destino= request.GET["ubB"]

      if tipo == "carpeta":
        os.system(f"cp -r {archivo}/ {destino}")
        mensaje="carpeta copiada con exito"
      else:
        os.system(f"cp {archivo} {destino}")
        mensaje="archivo copiado con exito"
    except:
      mensaje = ""
    ubicacion = getoutput("pwd")
    
    return render(request, "Copiar.html", {"ubicacion": ubicacion, "mensaje": mensaje})

def renombrar(request):
    return render(request,"Renombrar.html")

def mover(request):
    return render(request,"Mover.html")

def verPermisos(request):
    return render(request,"VerPermisos.html")

def cambiarPermisos(request):
    #ubi(dondestoy)
    try:
        tipo = request.POST["tipo"]
        permisos= str(request.POST["permisos"])
        nombre= request.POST["nombre"]
        if tipo == "carpeta":
            os.system(f"chmod -R {permisos} {nombre}")
        else:
            os.system(f"chmod {permisos} {nombre}")

        aviso="Se han cambiado los permisos con exito"
    except:
        aviso="Hay una falla"

    ubicacion= getoutput("pwd")
    return render(request,"CambiarPermisos.html",{"ubicacion":ubicacion,"aviso": aviso})

def cambiarPropietario(request):
    return render(request,"CambiarPropietario.html")

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
        #ubi(dondeestoy)
    except:
        mensaje="Carpeta prohibida"
    ubicacion= getoutput("pwd")
    #codigo de mostrar carpetas
    return render(render,"index.html", {"ubicacion":ubicacion})
