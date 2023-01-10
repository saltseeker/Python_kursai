import re

class Sakinys:
    
    
    
    def __init__(self, kurimo_tekstas):               #  def __init__ special class method - consturcot, automatically invoked on object creation (instructions how to create an object of this class)
        self.tekstas = kurimo_tekstas                 # self.tesktas, create a property for class and assign value saved in variable "kurimo_tekstas", which is passed during the creation of class instance.


    def atbulai(self):
        return self.tekstas[::-1] 
        


    def mazinti(self):
        return self.tekstas.lower()
        

    def didinti(self):
        return self.tekstas.upper()
        
    def parinkti_zodi(self, zodzio_indekas):
        zodziai = self.tekstas.split(" ")
        return zodziai[zodzio_indekas]

    def suskaiciuoti(self, ieskomas):
        return self.tekstas.count(ieskomas)

    def keisti(self, senas, naujas):
        return self.tekstas.replace(senas, naujas) 

    def analizuoti(self):
        zodziai = self.tekstas.split(" ")
        zodziu_kiekis = 0
        for zodis in zodziai:
            zodziu_kiekis += 1 if zodis.isalpha() else 0
            
        #zodziu_kiekis = len(self.tekstas.split(" ")) 
        skaiciu_listas = re.findall(r'\d+', self.tekstas)   #regix
        skaiciu_kiekis = 0
        for skaicius in skaiciu_listas:
            skaiciu_kiekis += len(skaicius)
        skaiciu_kiekis_isnumeric = 0
        for char in self.tekstas: 
            skaiciu_kiekis_isnumeric += 1 if char.isnumeric() else 0 
        didziuju_kiekis = 0
        for char in self.tekstas: 
            didziuju_kiekis += 1 if char.isupper() else 0 
        mazuju_kiekis = 0
        for char in self.tekstas: 
            mazuju_kiekis += 1 if char.islower() else 0 




    
                
                
                
                
        return  skaiciu_kiekis_isnumeric, didziuju_kiekis, mazuju_kiekis, zodziu_kiekis

        # didziosios =
        # mazosios =






sakinys = Sakinys("KazkAs 5534 KazKur 133")                               
sakinys2 = Sakinys("Nauji Metai")   

print(sakinys.atbulai())
print(sakinys.mazinti())
print(sakinys.didinti())
print(sakinys.parinkti_zodi(1))
print(sakinys.suskaiciuoti("Ka"))
print(sakinys.keisti("KazkAs", "Mano"))
print(sakinys.analizuoti())





