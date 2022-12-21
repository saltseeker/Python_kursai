metai = int(input("Iveskite metus: "))
if metai %4 == 0 and (metai %100 != 0 or metai %400==0):
    print("metai yra keliamieji")
else:
    print("nekeliamieji")
