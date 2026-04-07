class Ingredientes:
    def __init__(self, componentes, cantidaddeingredientes):
        self.componentes = componentes
        self.cantidaddeingredientes = cantidaddeingredientes

    def infoingredientes(self):
        lista = ", ".join(self.componentes)
        return f'Los ingredientes son ({self.cantidaddeingredientes}): {lista}'

if __name__ == "__main__":
    ingrediente1 = Ingredientes(["agua", "keratina", "aminoacido"], 3)
    print(ingrediente1.infoingredientes())