from django.shortcuts import render
import os
from subprocess import *
from django import forms
import re

dondestoy= "/raiz"

def home(request):
    try:
        os.chdir(getoutput("pwd")+dondestoy)
    except:
        mensaje="No existe el directorio"
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
    carpetas2 = [".."]
    for i in range(len(carpetas)):
        if (carpetas[i][2:] != ""):
            carpetas2.append(carpetas[i][2:])
    return carpetas2

def crear(request):
    try:
        os.chdir(getoutput("pwd")+dondestoy)
    except:
        mensaje="No existe el directorio"
    try:
        tipo= request.GET["tipo"]
        nombre= request.GET["nombre"]
        if tipo == "carpeta":
            os.system(f"mkdir {nombre}")
            aviso="La carpeta ha sido creada."
        else:
            os.system(f"touch {nombre}")
            aviso="El archivo ha sido creada."
    except:
        aviso=""
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request,"Crear.html",{"ubicacion":getoutput("pwd"),"aviso":aviso,"archivos2": iconos1, "carpetas2": iconos2})

def borrar(request):
    try:
        os.chdir(getoutput("pwd")+dondestoy)
    except:
        mensaje="No existe el directorio"
    try:
        tipo=request.GET["tipo"]
        nombre= request.GET["borrar"]
        if tipo== "carpeta":
            os.rmdir(nombre)
            aviso="La carpeta ha sido eliminada con exito."
        else:
            os.remove(nombre)
            aviso="El archivo ha sido eliminado con exito."
    except:
        aviso=""

    ubicacion= getoutput("pwd")
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request,"Borrar.html",{"ubicacion":getoutput("pwd"),"aviso":aviso,"archivos2": iconos1, "carpetas2": iconos2})

def copiar(request):
    
    try:
      tipo= request.GET["tipo"]
      archivo= str(request.GET["ubA"])
      destino= str(request.GET["ubB"])

      if tipo == "carpeta":
        try:
            os.system(f"cp -r {archivo}/ {destino}")
            mensaje="carpeta copiada con exito"
        except:
            mensaje= "No se puede copiar la carpeta."
      else:
        try:
            os.system(f"cp {archivo} {destino}")
            mensaje="Archivo copiado con exito"
        except:
            mensaje="No se puede copiar el archivo."
    except:
      mensaje = ""
    ubicacion = getoutput("pwd")
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    
    return render(request, "Copiar.html", {"ubicacion": ubicacion, "mensaje": mensaje,"archivos2": iconos1, "carpetas2": iconos2})

def renombrar(request):
    try:
        os.chdir(getoutput("pwd")+dondestoy)
    except:
        mensaje="No existe el directorio"
    try:
        viejo = str(request.POST["nombreV"])
        nuevo = str(request.POST["nombreN"])
        os.system(f"mv {viejo} {nuevo}")

        aviso = "Se ha cambiado el nombre con exito."

    except:
        aviso = ""

    ubicacion = getoutput("pwd")
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request,"Renombrar.html",{"ubicacion":ubicacion,"aviso": aviso,"archivos2": iconos1, "carpetas2": iconos2})

def mover(request):
    try:
      archivo= str(request.GET["nombre"])
      destino= str(request.GET["ubicacion"])
      try:
        os.system(f"mv {archivo} {destino} ")
        mensaje="El archivo/carpeta se ha movido con exito."
      except:
        mensaje= "No se puede mover la carpeta."
    except:
      mensaje = ""
    ubicacion = getoutput("pwd")
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    
    return render(request, "Mover.html", {"ubicacion": ubicacion, "mensaje": mensaje,"archivos2": iconos1, "carpetas2": iconos2})

def verPermisos(request):

    try:
        os.chdir(getoutput("pwd")+dondestoy)
    except:
        mensaje="No existe el directorio"

    try:

        tipo = request.GET["tipo"]

        nombre = request.GET["nombre"]

        permisos = ""

        if tipo == "carpeta":

            permisos = getoutput(f"ls -ld {nombre}")

            aviso = f"Los permisos de la carpeta {nombre} son {permisos[:10]}"

        else:

            permisos = getoutput(f"ls -l {nombre}")

            aviso = f"Los permisos del archivo {nombre} son {permisos[:10]}"

    except:

        aviso = ""


    ubicacion= getoutput("pwd")
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request,"VerPermisos.html",{"ubicacion": ubicacion,"aviso": aviso,"archivos2": iconos1, "carpetas2": iconos2})

def cambiarPermisos(request):
    try:
        os.chdir(getoutput("pwd")+dondestoy)
    except:
        mensaje="No existe el directorio"
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
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request,"CambiarPermisos.html",{"ubicacion":ubicacion,"aviso": aviso,"archivos2": iconos1, "carpetas2": iconos2})

def cambiarPropietario(request):

    try:
        os.chdir(getoutput("pwd")+dondestoy)
    except:
        mensaje="No existe el directorio"

    try:

        archivo = request.POST["archivo"]

        propietario = request.POST["propietario"]

        password = "Abril2026"

        os.system(f"echo {password} | sudo -S chown {propietario} {archivo}")

        aviso = f"Se ha cambiado el propietario de {archivo} con exito."

    except:

        aviso="Hay una falla"



    ubicacion= getoutput("pwd")
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request,"CambiarPropietario.html",{"ubicacion":ubicacion,"aviso": aviso,"archivos2": iconos1, "carpetas2": iconos2})


def abrir(request):
    global dondestoy
    global ruta
    try:
        nombre=request.GET['carpeta']
        if nombre=="..":
            aux= getoutput("pwd").split("/")
            aux.pop()
            aux1= "/".join(aux)
            os.chdir(aux1)
            dondestoy=aux.pop()
        else:
            dondestoy= '/' +nombre
            os.chdir(getoutput("pwd")+dondestoy) 
    except:
        aviso=""
    iconos1 = mostrar_archivos()
    iconos2 = mostrar_carpetas()
    return render(request,"index.html", {"ubicacion":getoutput("pwd"),"archivos2": iconos1, "carpetas2": iconos2,"aviso":""})
