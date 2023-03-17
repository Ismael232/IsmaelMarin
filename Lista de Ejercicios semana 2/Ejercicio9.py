### Minisistema
roles=['admin','vendedor','inventario']

sistema={
    "nombre":"tienda",
    "usuarios":[
        {
            'name':"",
            'password':"",
            'rol':"" ##vendedor ,administrador ,inventario
        }
    ],
    "sedes":[{
        "nombreSede":"",
        "ubicacion":""
    }],
    "productos":[
    {
        "nombre":"",
        "precio":"",
        "stock":""
    }]
}
##### funciones
## karen vera
def agregarUsuario():
    nameUsuario=input("ingrese el nombre de usuario: ")
    password=input("ingrese su password: ")
    while True:
        rol=input("ingrese su rol: ")
        if rol in roles:
            break
        else:
            print("ingrese un rol correcto: ",roles)
    
    dictUser={
        'name':nameUsuario,
        'password':password,
        'rol':rol
    }
    sistema['usuarios'].append(dictUser)
###
def eliminarUsuario():
    usuarioPorEliminar=input("ingrese usuario por eliminar: ")
    for i,valor in enumerate(sistema['usuarios']):
        if valor['name']==usuarioPorEliminar:
                ## ingresar password para verificar que es correcto
                sistema['usuarios'].remove(i)
    ## remove
    pass
###
def obtenerRol(usuario):
    rol=""
    for i,valor in enumerate(sistema["usuarios"]):
        if valor['name']==usuario:
            rol=valor['rol']
    return rol
####
def agregarSede():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        sede=input("ingrese sede: ")
        ubicacion=input("ingrese ubicacion: ")
        dictSede={
            'nombreSede':sede,
            'ubicacion':ubicacion
        }
        sistema["sedes"].append(dictSede)
    else:
        print("no es un rol permitido")
###
def agregaruUsuarios():
    while True:
        agregarUsuario()
        respuesta = input("Desea agregar otro usuario? Si/No: ")
        if respuesta.upper() == "NO":
            break
def agregarSedes():
    while True:
        agregarSede()
        respuesta = input("Desea agregar otra sede? Si/No: ")
        if respuesta.upper() == "NO":
            break

def verSedes():
    for i,sede in sistema["sedes"]:
        print(sede['nombreSede'])
    pass
#####
def agregarProductos():
    pass
#####
def cambiarStock():
    pass

agregaruUsuarios()
agregarSedes()
#verSedes()