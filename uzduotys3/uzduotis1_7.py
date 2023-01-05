# Gražintų, ar paduotas skaičius yra pirminis.


n= int(input("iveskite skaiciu: "))
def ar_pirminis(skaicius):
    if skaicius > 1:
        for num in range(2, skaicius):
            if skaicius % num == 0:
                return "nepirminis"
        return "pirminis"
    return "nepirminis"

print(ar_pirminis(n))