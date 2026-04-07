from shampoo import Shampoo

if __name__ == "__main__":
    shampooo1 = Shampoo("antiedad", "tio nacho", ["agua", "mentol","sulfato"],3,"botella",300,"vidrio",5.8)
    shampoo2 = Shampoo("hidratante", "pantene", ["keratina","maicena","vitamina e","agua"],4,"dispensador",1000,"plastico",6.5)
    shampoo3= Shampoo("suave para bebes", "arruru",["agua","gliceerina","manzanilla"],3,"botella",200,"plastico",6.8)
    #polimorfismo
    print(shampooo1.describir())
    print(shampoo2.describir())
    print(shampoo3.describir())
    
    #str de cada objeto
    print(shampooo1)
    print(shampoo2)
    print(shampoo3)
    #metodos propios de ingedientes y envase
    print(shampooo1.infoingredientes())
    print(shampoo2.infoenvase())
    #encapsulamiento
    print("ph actual de antiedad es",shampooo1.ph)
    #modidicacion del ph con el setter
    shampooo1.ph= 5.5
    print ("Nuevo ph ", shampooo1.ph)
    
     #modicacion invalida
    
    shampooo1.ph=8.0