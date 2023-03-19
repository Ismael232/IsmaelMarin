class Producto:
    nombre = ""
    codigo = ""

    def __init__(self,nombre,codigo) -> None:
        self.nombre = nombre
        self.codigo = codigo
    def desfragmentandoCodigo(self) -> str:
        lista = []
        pais = self.codigo.split("-",3)[0] 
        lote = self.codigo.split("-",3)[1] 
        year = self.codigo.split("-",3)[2]
        lista.append(pais)
        lista.append(lote)
        lista.append(year)
        return lista
    
    def __str__(self) -> str:
        codigo = self.desfragmentandoCodigo()
        return f"El producto proviene de {codigo[0]} y del lote {codigo[1]}"
    
if __name__ == "__main__":
    producto1 = Producto("Camisa","Peru-0002-2013")
    print(producto1)




