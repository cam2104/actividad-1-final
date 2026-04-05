class Electrico:
    def __init__(self, bateria):
        self.bateria = bateria

    def cargar_bateria(self):
        return f"Cargando batería al {self.bateria}%"