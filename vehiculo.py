from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
    
if __name__ == "__main__":
    print("Vehiculo es una clase abstracta, no se puede instanciar directamente.")