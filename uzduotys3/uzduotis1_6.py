

#Gražintų, ar paduotas skaičius yra pirminis.


def unikalus_sarasas(sarasas):
    naujas_sarasas = []
    for skaicius in sarasas:
        if skaicius not in naujas_sarasas:
            naujas_sarasas.append(skaicius)
    return naujas_sarasas


print(unikalus_sarasas([234, 234, "kazkas", "kazkur", 13, "kazkas"]))
