
# Sukurkite sarašą skaičių nuo 1 iki 52
# Importuokite iš random modulio shuffle
# Išmaišykite sąrašo elementus atsitiktine tvarka
# Bonus: vietoj elementų skaičių, sugeneruokite saraše kortų kaladės reikšmes.

from random import shuffle


#skaiciai = list(range(2, 10))
paveiksliukas = ["\u2660", "\u2663", "\u2665", "\u2666"]
raides = [*range(2, 10), "J", "Q", "K", "A"]

kortos = []
for paveiksliukas in paveiksliukas:
    for raides in raides:
        kortos.append(f"{raides} {paveiksliukas}")



shuffle(kortos)
print(kortos)



# "*" args ispakuoja sarasa