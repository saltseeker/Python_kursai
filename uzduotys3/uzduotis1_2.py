
## 2. Gražintų paduoto sąrašo iš skaičių, sumą.


sarasas = [1, 3, 4, 5]

def saraso_suma(sarasas):
    suma=0
    for skaicius in sarasas:
      suma += skaicius
    return suma
print(saraso_suma(sarasas))