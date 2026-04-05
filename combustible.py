class Combustible:
    def __init__(self, nivel_gasolina):
        self.nivel_gasolina = nivel_gasolina

    def repostar(self):
        return f"Repostando gasolina: {self.nivel_gasolina} litros"