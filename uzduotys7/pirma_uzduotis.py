class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai 
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas



    def __str__(self):
        return f"\n{self.__class__.__name__}\nKokiu metu: {self.metai},\nKoks modelis: {self.modelis}, \nKoks Tipas: {self.kuro_tipas}" 

    def vaziuoti(self):
        print("vaziuoja ir")

    def stoveti(self):
        print("parkuojasi")

    def pildyti_degalus(self):
        print("isipila degalus")


    



class Elektromobilis(Automobilis):

    def pildyti_degalus(self):
        print("baterija ikrauta")

    def  vaziuoti_autonomiskai(self):
        print("vaziuoja autonomiskai")


mazda = Automobilis (1990, "mazda", "benzinas")
print(mazda)
mazda.vaziuoti()
mazda.stoveti()
mazda.pildyti_degalus()


tesla = Elektromobilis (2023, "Tesla", "Elektra")
print(tesla)
tesla.vaziuoti()
tesla.stoveti()
tesla.pildyti_degalus()
tesla.vaziuoti_autonomiskai()
