
from kiti_zaislai import geris


kintamasis = "Geras pirmas rytas"


def atbulai(stringas):
    return stringas[::-1]

print(f"mano moduliukas {__name__} sekmingai importuotas ir veikia")
print(geris.geras)

if __name__ == "__main__":                         #apribojam kad nespausdintu                     
    print("testuojam", kintamasis)
   