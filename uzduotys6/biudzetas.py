class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    
    def __str__(self):
        return f"{self.tipas} {self.suma}"

    def __add__(self, other):
        return (self.suma if self.tipas == "Pajamos" else self.suma * -1) + other

    
    def __iadd__(self, other):
         return (self.suma if self.tipas == "Pajamos" else self.suma * -1) + other 
    

    def __radd__(self, other):
        return (self.suma if self.tipas == "Pajamos" else self.suma * -1) + other



# irasas = Irasas("Pajamos", 11) 
# irasas2 = Irasas("islaidos", 20) 
# suma = sum([irasas, irasas2])
# print(suma, "summa")
# print(irasas + irasas2)
# irasas2 += irasas
# print(irasas2)


class Biudzetas:
    def __init__(self):
        self.zurnalas=[]

    def prideti_pajamu_irasa(self, suma):
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)

    
    def prideti_islaidu_irasa(self, suma):
        islaidos = Irasas("Islaidos", suma)
        self.zurnalas.append(islaidos)


    def gauti_balansa(self):  
        return sum(self.zurnalas)
             

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)



biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - pajamos, \n\n2 - islaidos, \n\n3 - balansas, \n\n4 - ataskaita, \n\n9 - iseiti "))
    if pasirinkimas == 1:
        suma = int(input("iveskite pajamas: "))
        biudzetas.prideti_pajamu_irasa(suma)
    if pasirinkimas == 2:
        suma = int(input("iveskite islaidas: "))
        biudzetas.prideti_islaidu_irasa(suma)
    if pasirinkimas == 3:
        print(biudzetas.gauti_balansa())
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        break




# class Pajamos:
#     def __init__(self):


# class Islaidos:
#     def __init__(self):
        
                
        

# class Person:
#     def __init__(self, vardas, pavarde, amzius):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
        

#     def __str__(self) -> str:
#         return f'{self.vardas} {self.pavarde} {self.amzius}'


# zmogus = Person("Kestutis", "Bauzys", 33)  
# print(zmogus)
