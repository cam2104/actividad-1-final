class Envase:
    def __init__(self,tipoenvase, mililitros, material):
        self.tipoenvase = tipoenvase
        self.mililitros = mililitros
        self.material = material
    
    def infoenvase(self):
        return f'el envase es de tipo {self.tipoenvase}, tiene capacidad de {self.mililitros}, y es de material {self.material}'

if __name__=="__main__":
    envase1 = Envase("botella",500,"plastico")
    print(envase1.infoenvase())
    