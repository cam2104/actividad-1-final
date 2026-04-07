from producto import Producto
from ingredientes import Ingredientes
from envase import Envase

class Shampoo(Producto, Ingredientes, Envase):
    def __init__(self, nombre, marca, componentes, cantidadeingredientes, tipoenvase, mililitros, material, ph):
        Producto.__init__(self, nombre, marca)
        Ingredientes.__init__(self, componentes, cantidadeingredientes)
        Envase.__init__(self, tipoenvase, mililitros, material)
        self.ph = ph
        
    def describir(self):
        return f'el shampoo {self.nombre} de {self.marca} tiene un ph de {self.ph}'
    
    def __str__(self):
        return (f'shampoo: {self.nombre} marca: {self.marca} ph: {self.ph}'
                f'mililitros:{self.mililitros} ph:{self.ph}')
                
    @property
    def ph(self):
        return self._ph
    @ph.setter
    def ph(self, nuevoph):
        if not(4.5<= nuevoph <=7.0):
            print(f'ph invalido: {nuevoph} debe estar entre 4.5 y 7.0 para no dañar el cabllo')
        else:
            self._ph = nuevoph

if __name__ == "__main__":
    shampoo1 = Shampoo("shampoo anticaspa","loreal",["agua", "aloe vera"],2, "botella",400,"plastico",5.5)
    print(shampoo1.describir())