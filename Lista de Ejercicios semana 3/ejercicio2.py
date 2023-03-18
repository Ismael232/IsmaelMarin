## Tienda de autopartes
class Producto:
    id = 0
    nombre = ""
    precio = 0.0
    stock = 0
    
    def __init__(self,id,nombre,precio,stock) -> None:
        self.id =  id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self) -> str:
        return f"{self.id} Producto {self.nombre} con precio {self.precio} y stock {self.stock}"
class Catalogo:
    lista = []
    
    def __init__(self) -> None:
        self.lista = []
    def agregarProducto(self,producto:Producto):
        self.lista.append(producto)
    def mostrarProductos(self):
        productos = []
        for producto in self.lista:
            productos.append(producto.nombre)
        print(productos)

producto1 = Producto(1,"cama", 12.25, 1)
producto2 = Producto(2,"asiento", 4.25, 2)
producto3 = Producto(3,"rama", 12.4, 5)

catalogo = Catalogo()
catalogo.agregarProducto(producto1)
catalogo.agregarProducto(producto2)
catalogo.agregarProducto(producto3)
catalogo.mostrarProductos()
