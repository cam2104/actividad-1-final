from carro import Carro

if __name__ == "__main__":
    carro1 = Carro("Toyota", "Corolla", 80, 40, 60)
    carro2 = Carro("Tesla", "Model S", 100, 0, 120)
    carro3 = Carro("Ford", "Fiesta", 50, 30, 80)

    print(carro1.arrancar())
    print(carro2.arrancar())
    print(carro3.arrancar())

    print(carro1)
    print(carro2)
    print(carro3)

    print("\nVelocidad actual:", carro1.velocidad)

    carro1.velocidad = 90
    print("Nueva velocidad:", carro1.velocidad)

    carro1.velocidad = -10