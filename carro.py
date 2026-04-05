from vehiculo import Vehiculo
from electrico import Electrico
from combustible import Combustible

class Carro(Vehiculo, Electrico, Combustible):
    def __init__(self, marca, modelo, bateria, nivel_gasolina, velocidad):
        Vehiculo.__init__(self, marca, modelo)
        Electrico.__init__(self, bateria)
        Combustible.__init__(self, nivel_gasolina)

        self._velocidad = velocidad

    def arrancar(self):
        return f"El carro {self.marca} {self.modelo} está arrancando"

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} | Velocidad: {self._velocidad} km/h"

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        if nueva_velocidad < 0:
            print("❌ La velocidad no puede ser negativa")
        else:
            self._velocidad = nueva_velocidad