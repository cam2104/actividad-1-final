from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca
        
        @abstractmethod
        def descripcion(self):
            pass
        
        @abstractmethod
        def __str__(self):
            pass
        
if __name__ == "__main__":
    print("no se puede instanciaar directamente")
    