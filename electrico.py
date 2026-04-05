class Electrico:
    def __init__(self, bateria):
        self.bateria = bateria

    def cargar_bateria(self):
        return f"Cargando bateria al {self.bateria}%"

if __name__ == "__main__":
    e = Electrico(85)
    print(e.cargar_bateria())