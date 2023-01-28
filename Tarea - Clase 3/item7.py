class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Producto: {self.nombre}, Código: {self.codigo}"

    def identificar_pais(self):
        pais = self.codigo.split("-")[0]
        return pais

    def identificar_lote(self):
        lote = self.codigo.split("-")[1]
        return lote

    def identificar_anio(self):
        anio = self.codigo.split("-")[2]
        return anio