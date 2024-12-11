from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.apps import apps
#import firebase_admin
 
# Hacemos uso de credenciales que nos permitirán usar Firebase Admin SDK 
#from firebase_admin import credentials
 
# Importo el Servicio Firebase Realtime Database 
#from firebase_admin import db


def connectDB():
    #if not firebase_admin._apps:
     #   cred = credentials.Certificate("./biltec-5cf10-firebase-adminsdk-ayq1p-7398637814.json")
     #   firebase_admin.initialize_app(cred, {
      #      "databaseURL": "https://biltec-5cf10-default-rtdb.firebaseio.com/" #Your database URL
     #   })
    dbconn = db.reference("Objeto")
    ref = db.reference('Objeto')
    print(ref.get())
    return dbconn

def tabla(request):
    objetos = []
    dbconn = connectDB()
    tblObjeto = dbconn.get()
    print("1")
    
    for key, value in tblObjeto.items():
        # Asegúrate de que value sea un diccionario antes de intentar acceder a sus claves
        if isinstance(value, dict):
            objetos.append({"id": value["id"],"nombre": value["nombre"],"description": value["description"],"disponibles": value["disponibles"],"ubicacion": value["ubicacion"],})
    print(objetos)
    print("2")
    return render(request, 'pagina/tabla.html', {'objetos': objetos})


def index(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
        
    if result:
        print(result)
        print("hola estoy en index")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/index.html',context)
    else:
        print("hola estoy en index")
        context={}
        return render(request, 'pagina/index.html',context)

def contacto(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
    if result:
    
        print("hola estoy en contacto")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/contacto.html',context)
    else:
        print("hola estoy en contacto")
        context={}
        return render(request, 'pagina/contacto.html',context)

def nosotros(request):

    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False

    if result:
        print("hola estoy en nosotros")
        sesion=request.session["sesion"]
        context = {'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/nosotros.html',context)
    else:    
        print("hola estoy en nosotros")
        context={}
        return render(request, 'pagina/nosotros.html',context)
    
def preguntas(request):

    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False

    if result:
        print("hola estoy en nosotros")
        sesion=request.session["sesion"]
        context = {'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/preguntas.html',context)
    else:    
        print("hola estoy en preguntas")
        context={}
        return render(request, 'pagina/preguntas.html',context)

def servicios(request):

    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False

    if result:
        print("hola estoy en servicios")
        sesion=request.session["sesion"]
        context = {'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/servicios.html',context)
    else: 
        print("hola estoy en servicios")
        context={}
        return render(request, 'pagina/servicios.html',context)

def inicio(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False
        
    if result: 
        print("hola estoy en inicio")
        context = {'sesion':result,'tipo':tipo}
        return render(request, 'pagina/inicio.html',context)

    else:  
        print("hola estoy en inicio")
        context={}
        return render(request, 'pagina/inicio.html',context)

def inventarioadmin(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        objetos = []
        dbconn = connectDB()
        tblObjeto = dbconn.get()
        
        for key, value in tblObjeto.items():
         # Asegúrate de que value sea un diccionario antes de intentar acceder a sus claves
            if isinstance(value, dict):
                objetos.append({
                    "id": value["id"],
                    "nombre": value["nombre"],
                    "description": value["description"],
                    "disponibles": value["disponibles"],
                    "ubicacion": value["ubicacion"],
                })    
            else: 
                context = {'sesion':result,'tipo':tipo}
                return render(request, 'pagina/inventarioadmin.html',context)
                
        context = {'objetos': objetos,'sesion':result,'tipo':tipo}
        return render(request, 'pagina/inventarioadmin.html',context)
    
    else:    
        return render(request,'pagina/nosesion.html')

def inventarioworker(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        objetos = []
        dbconn = connectDB()
        tblObjeto = dbconn.get()
        context = {'sesion':result,'tipo':tipo}
        for key, value in tblObjeto.items():
         # Asegúrate de que value sea un diccionario antes de intentar acceder a sus claves
            if isinstance(value, dict):
                objetos.append({
                    "id": value["id"],
                    "nombre": value["nombre"],
                    "description": value["description"],
                    "disponibles": value["disponibles"],
                    "ubicacion": value["ubicacion"],
                })
        context={'sesion':result,'tipo':tipo,'objetos': objetos}
        return render(request, 'pagina/inventarioworker.html',context)
    else:    
        return render(request,'pagina/nosesion.html')
    
def agregar(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("hola estoy en agregar")
        context={'sesion':result,'tipo':tipo}
        return render(request,'pagina/agregar.html',context)
    else:    
        return render(request,'pagina/nosesion.html')
    
    
    
def editar(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("hola estoy en modificar")
        context={'sesion':result,'tipo':tipo}
        return render(request,'pagina/editar.html',context)
    else:    
        return render(request,'pagina/nosesion.html')

def nosesion(request):
    print("hola estoy en no hay sesion")
    context={}
    return render(request,'pagina/nosesion.html',context)

def usuarioAdmi(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("hola estoy en lista de usuarios")
        usuarios = Usuario.objects.all()
        context={'usuarios':usuarios,'sesion':result,'tipo':tipo}
        return render(request,'pagina/usuarioadmin.html',context)
    else:    
        return render(request,'pagina/nosesion.html')

def validar(request):
        print("Estoy en el validar credenciales")
        context={}

        if request.method == "POST":
            usuarioV = request.POST['usuario']
            contraV = request.POST['contra']
            opcion = request.POST['opcion']
            usuarios = Usuario.objects.all()
            inventario = Objeto.objects.all()
            if opcion == "Ingresar":
                for usuario in usuarios:
                    if usuarioV == usuario.username and contraV == usuario.password and usuario.tipo == "admin":
                        tipo = usuario.tipo
                        request.session["sesion"]=usuario.username
                        sesion=request.session["sesion"]
                        print("Usuario y contraseña Correctos")
                        context={'sesion':sesion,'inventario':inventario,'tipo':tipo}

                        return render(request,'pagina/inicio.html',context)
                    
                    elif usuarioV == usuario.username and contraV == usuario.password and usuario.tipo == "worker":
                        tipo = usuario.tipo
                        request.session["sesion"]=usuario.username
                        sesion=request.session["sesion"]
                        print("Usuario y contraseña Correctos")
                        context={'sesion':sesion,'inventario':inventario,'tipo':tipo}

                        return render(request,'pagina/inicio.html',context)
                        
                    else:
                        print("Usuario o contraseña incorrectos")
                        
                return render(request,'pagina/error.html',context)
    
def login(request):
    print("estoy en login")
    context={}
    return render(request,'pagina/ingreso.html',context)

def error(request):
    print("error")
    context={}
    return render (request,'pagina/error.html',context)

def salir_error(request):
    print("redirigir al ingreso")
    context={}
    if request.method =="POST":
        opcion = request.POST['opcion']
        if opcion =="Volver a ingresar":
            return render (request,'pagina/ingreso.html',context)
        else:
            return render(request,'pagina/inicio.html')
        
def volver_tabla(request):
    print("volviendo a la tabla")
    context={}
    return render (request,'pagina/inventario.html',context)

def cerrar(request):
    print("Hola estoy en cerrar")
    if 'sesion' in request.session:
        del request.session['sesion']
        
        print("La sesión se ha cerrado exitosamente.")
    else:
        print("La clave 'sesion' no está presente en la sesión.")

    context = {}
    return render(request, "pagina/inicio.html", context)

def producto_add(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
            objetos = []
            dbconn = connectDB()
            tblObjeto = dbconn.get()
            if request.method == 'POST':
                id = request.POST['id']
                nombre = request.POST['nombre']
                description = request.POST['description']
                disponibles = request.POST['disponibles']
                ubicacion = request.POST['ubicacion']
                dbconn = connectDB()
                dbconn.push( { "id": id, "nombre": nombre, "description": description, "disponibles": disponibles, "ubicacion": ubicacion })
                context={'objetos':objetos,'tipo':tipo,'sesion':result}
                for key, value in tblObjeto.items():
                    if isinstance(value, dict):
                        objetos.append({
                            "id": value["id"],
                            "nombre": value["nombre"],
                            "description": value["description"],
                            "disponibles": value["disponibles"],
                            "ubicacion": value["ubicacion"],
                        })
            context={'objetos':objetos,'tipo':tipo,'sesion':result}    
            return render(request, 'pagina/inventarioadmin.html',context)
    else:    
        return render(request,'pagina/nosesion.html')
   
def producto_edit(request,key):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False
    if result:
        print("estoy en la pagina editar producto")
        sesion= request.session["sesion"]
        objetos = Objeto.objects.all()

        for producto in objetos:
            if producto.id ==key:
                break
        context={'objetos':objetos,'tipo':tipo,'sesion':sesion}
        return render(request,'pagina/editar.html',context)
    else:    
        return render(request,'pagina/nosesion.html')

def producto_editar(request, id):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("Estoy en la función modificar")
        context = {}
        objetos = Objeto.objects.all()
        aviso = ""

        lista = []
        dbconn = connectDB()
        tblObjetos = dbconn.get()

        if request.method == 'GET':
            for key, value in tblObjetos.items():
                if(value["id"] == id):
                    global updatekey
                    updatekey = key
                    lista.append({"id": value["id"],"nombre": value["nombre"],"description": value["description"],"disponibles": value["disponibles"],"ubicacion": value["ubicacion"]})
            return render(request, 'editar.html', {'obj':lista[0]})

        if request.method == "POST":
            id = request.POST['id']
            nombre = request.POST['nombre']
            description = request.POST['description']
            disponibles = request.POST['disponibles']
            ubicacion  = request.POST['ubicacion']
            opcion = request.POST['opcion']


            if opcion == "Modificar ítem":
                try:

                    updateitem = dbconn.child(updatekey)
                    updateitem.update( { "id": id, "nombre": nombre, "description": description, "disponibles": disponibles, "ubicacion": ubicacion } )

                    context = {'objetos': objetos, 'aviso': aviso,'tipo':tipo,'sesion':result}
                    aviso = "Producto modificado"

                except Objeto.DoesNotExist:
                    aviso = "El producto no existe"

            context = {'objetos': objetos, 'aviso': aviso,'tipo':tipo,'sesion':result}
            return render(request, 'pagina/inventarioadmin.html', context)
    else:    
        return render(request,'pagina/nosesion.html')
    

def producto_findEdit(request,producto_id):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False



    if result:
        if key !="":
            modlist = []
            dbconn = connectDB()
            tblCars = dbconn.get()

            for key, value in tblCars.items():
                if(value["id"] == producto_id):
                    global updatekey
                    updatekey = key
                    print(updatekey)
                    modlist.append({ "id": value["id"],"nombre": value["nombre"],"description": value["description"],"disponibles": value["disponibles"],"ubicacion": value["ubicacion"]})


            producto= Objeto.objects.get(id=key)
            context={'modlist':modlist,'tipo':tipo,'sesion':result}
            if producto:
                return render(request,'pagina/editar.html',context)

            else:
                context={'mensaje':"id no encontrada",'tipo':tipo,'sesion':result}
                return render (request,'pagina/inventarioadmin.html')
    else:    
        return render(request,'pagina/nosesion.html')
    
def producto_del(request,producto_id):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("estoy en la funcion eliminar producto")

        try:
            objetos=[]
            dbconn = connectDB()
            tblObjetos = dbconn.get()
            for key, value in tblObjetos.items():
                if(value["id"] == producto_id):
                    deletekey = key
                    print(deletekey)
                    break
            delitem = dbconn.child(deletekey)
            delitem.delete()
            dbconn = connectDB()
            tblObjetos = dbconn.get()
            for key, value in tblObjetos.items():
                    if isinstance(value, dict):
                        objetos.append({
                            "id": value["id"],
                            "nombre": value["nombre"],
                            "description": value["description"],
                            "disponibles": value["disponibles"],
                            "ubicacion": value["ubicacion"],
                        })
            context={'objetos':objetos,'mensaje':mensaje,'tipo':tipo,'sesion':result}
            return render(request,'pagina/inventarioadmin.html',context)
        except:
            dbconn = connectDB()
            tblObjetos = dbconn.get()
            for key, value in tblObjetos.items():
                    if isinstance(value, dict):
                        objetos.append({
                            "id": value["id"],
                            "nombre": value["nombre"],
                            "description": value["description"],
                            "disponibles": value["disponibles"],
                            "ubicacion": value["ubicacion"],
                        })
            mensaje="error id no encontrado"
            context={'objetos':objetos,'mensaje':mensaje,'tipo':tipo,'sesion':result}
            return render(request,'pagina/inventarioadmin.html',context)
    
    else:    
        return render(request,'pagina/nosesion.html')
    
def usuario_agregar(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:

        print("hola estoy en agregar usuario")
        context={'tipo':tipo,'sesion':result}
        return render(request,'pagina/usuario_agregar.html',context)
    else:    
        return render(request,'pagina/nosesion.html')
    
def usuario_add(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("Estoy en la función agregar usuario")
        
        context = {}

        if request.method == "POST":

            correo = request.POST['correo']
            username = request.POST['username']
            password = request.POST['password']
            tipo = request.POST['tipo']
            opcion = request.POST['opcion']
            
            if opcion == "Agregar usuario":
                
                usuario = Usuario(
                    
                    correo = correo,
                    username = username,
                    password = password,
                    tipo = tipo
                    )
                usuario.save() 
                
                usuarios = Usuario.objects.all()
                context={'usuarios':usuarios,'tipo':tipo,'sesion':result}
                return render(request, 'pagina/usuarioadmin.html', context)
    else:    
        return render(request,'pagina/nosesion.html')

def usuario_findEdit(request,key):
    
    if key !="":
        usuario= Usuario.objects.get(correo=key)
        context={'usuario':usuario}
        if usuario:
            return render(request,'pagina/usuario_editar.html',context)

        else:
            context={'mensaje':"correo no encontrado"}
            return render (request,'pagina/usuarioadmin.html')   
             
def usuario_edit(request,key):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("estoy en la pagina editar usuario")
        usuarios = Usuario.objects.all()

        for usuario in usuarios:
            if usuario.correo ==key:
                context={'usuario':usuario,'tipo':tipo,'sesion':result}
                break
        return render(request,'pagina/usuario_editar.html',context)
    else:    
        return render(request,'pagina/nosesion.html')
    
def usuario_editar(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("Estoy en la función modificar usuario")
        usuarios = Usuario.objects.all()
        aviso = ""
        context = {'tipo':tipo,'sesion':result}
        if request.method == "POST":
            correo = request.POST['correo']
            username = request.POST['username']
            password = request.POST['password']
            tipo = request.POST['tipo']
            opcion = request.POST['opcion']

            if opcion == "Modificar usuario":
                try:
                    usuario = Usuario.objects.get(correo=correo)

                    usuario.username = username
                    usuario.password = password
                    usuario.tipo = tipo

                    usuario.save()
                    
                    aviso = "Usuario modificado"
                    
                except Usuario.DoesNotExist:
                    aviso = "El producto no existe"
            context = {'usuarios': usuarios, 'aviso': aviso,'tipo':tipo,'sesion':result}
            
        return render(request, 'pagina/usuarioadmin.html', context)
    else:    
        return render(request,'pagina/nosesion.html')

def usuario_del(request,key):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
    else:
        result = False

    if result:
        print("estoy en la funcion eliminar usuario")
        try:
            usuario= Usuario.objects.get(correo=key)
            usuario.delete()
            usuarios = Usuario.objects.all()
            context={'usuarios':usuarios,'tipo':tipo,'sesion':result}
            return render(request,'pagina/usuarioadmin.html',context)
        except:

            usuarios = Usuario.objects.all()
            context={'usuarios':usuarios,'tipo':tipo,'sesion':result}
            return render(request,'pagina/usuarioadmin.html',context)
    else:    
        return render(request,'pagina/nosesion.html')
    
def evento1(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
    if result:
    
        print("hola estoy en evento1")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/evento1.html',context)
    else:
        print("hola estoy en evento1")
        context={}
        return render(request, 'pagina/evento1.html',context)
    
def evento2(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
    if result:
    
        print("hola estoy en evento2")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/evento2.html',context)
    else:
        print("hola estoy en evento2")
        context={}
        return render(request, 'pagina/evento2.html',context)
    
def evento3(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
    if result:
    
        print("hola estoy en cevento3")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/evento3.html',context)
    else:
        print("hola estoy en evento3")
        context={}
        return render(request, 'pagina/evento3.html',context)

def evento4(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
    if result:
    
        print("hola estoy en evento4")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/evento4.html',context)
    else:
        print("hola estoy en evento4")
        context={}
        return render(request, 'pagina/evento4.html',context)
    
def evento5(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
    if result:
    
        print("hola estoy en evento5")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/evento5.html',context)
    else:
        print("hola estoy en evento5")
        context={}
        return render(request, 'pagina/evento5.html',context)    
    
def evento6(request):
    if "sesion" in request.session:
        result = request.session["sesion"]
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.username == result:
                tipo = usuario.tipo
                break
            else:
                tipo = 0
    else:
        result = False
    if result:
    
        print("hola estoy en evento6")
        sesion=request.session["sesion"]
        context={'sesion':sesion,'tipo':tipo}
        return render(request, 'pagina/evento6.html',context)
    else:
        print("hola estoy en contacto")
        context={}
        return render(request, 'pagina/evento6.html',context)