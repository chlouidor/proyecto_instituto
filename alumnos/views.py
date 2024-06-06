from django.shortcuts import render
from .models import Genero,Alumno

# Create your views here.

def index(request):
    context={}
    return render (request,"alumnos/index.html",context)

def crud(request):
    alumnos = Alumno.object.all()
    context = {"alumnos" :alumnos}
    return render (request,"alumnos_list.html",context)

def alumnosADD(request):
    if request.method !="POST":
        generos =Genero.object.all()
        context={"generos":generos}
        return render (request,"alumnos/alumnos_add.html",context)
    else:
        print("Entra por aqui")
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["aPaterno"]
        aMaterno = request.POST["aMaterno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo="1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = {"mensaje":"ok datos guardados........."}
        return render(request,"alumnos/alumnos_add.html",context)
