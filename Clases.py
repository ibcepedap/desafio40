class Estudiante:
    def __init__(self,n,p,f) -> None:
        self.nombre = n
        self.parcial = p
        self.final = f

    def __str__(self):
         txt = (self.nombre + " P = " + str(self.parcial) + " F = " + str(self.final))
         return txt

# Nota es 30% examen parcial y 70% examen final

    def calcular_nota(self):
        nota = (self.parcial * 0.3) + (self.final * 0.7)
        return nota
    
    def supera(self,n):
            return (self.calcular_nota() >= n)
    
    def aprueba(self):
         aprueba = self.supera(50)
         return aprueba
    
ali = Estudiante("Alicia", 40, 100)
benji = Estudiante("Benjamin", 60, 80)

print(ali)
print(benji)

nali = ali.calcular_nota()
print("Alicia tiene de nota un ",nali)
nbenji = benji.calcular_nota()
print("Benjamin tiene de nota un ",nbenji)

ali60 = ali.supera(60)
print ("Alicia supera los 60 puntos ",ali60)
ali90 = ali.supera(90)
print ("Alicia supera los 90 puntos ",ali90)

aliaprueba = ali.aprueba()
print("Alicia aprueba? ", aliaprueba)