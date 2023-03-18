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
    usuario=input("ingresa usuario: ")
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
    sedes = []
    for i,sede in enumerate(sistema["sedes"]):
        sedes.append(sede['nombreSede'])
    pass
    print(sedes)
#####
def agregarProducto():
    nombreProducto=input("ingrese el nombre del producto: ")
    stock=int(input("ingrese el stock: "))
    while stock <= 0:
        print("El valor para el stock no es valido")
        stock=int(input("ingrese el stock: "))
        if stock > 0:
            break
    precio=float(input("ingrese el precio: "))
    while precio <= 0:
        print("El valor de precio no es valido")
        precio=float(input("ingrese el precio: "))
        if precio > 0:
            break
    
    dictProduc={
        'nombre':nombreProducto,
        'precio':precio,
        'stock':stock
    }
    sistema['productos'].append(dictProduc)

def agregarProductos():
    while True:
        agregarProducto()
        respuesta = input("Desea agregar otro producto? Si/No: ")
        if respuesta.upper() == "NO":
            break
#####
def cambiarStock():
    nombre = input("Nombre del producto: ")
    comprobador = True
    for i,valor in enumerate(sistema["productos"]):
       if valor['nombre'] == nombre:
           nuevoStock = int(input("Ingrese nuevo stock: "))
           comprobador = False
           if nuevoStock >= 0:
               valor['stock'] = nuevoStock
               break
    if comprobador:
        print("El producto no se encuentra") 
           
#agregaruUsuarios()
#agregarSedes()
#verSedes()
#agregarProductos()
#cambiarStock()
