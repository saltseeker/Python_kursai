
# 3.Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).



def didelis_skaicius(*args):
    didziausias = args[0]
    for argas in args:
        if argas > didziausias:
            didziausias = argas
    return didziausias
print(didelis_skaicius(43, 3123, 111, 53453, 3123123))
