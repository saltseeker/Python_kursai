pirmas_skaicius = int(input("Iveskite pirma skaciui: "))
antras_skaicius = int(input("Iveskite antra skaiciu: "))
operacija = input("koki veiksma atlikti(+, -, /, *): ")


if operacija == "+":
    rezultatas = pirmas_skaicius + antras_skaicius
elif operacija == "-":
    rezultatas = pirmas_skaicius - antras_skaicius
elif operacija == "/":
    rezultatas = pirmas_skaicius / antras_skaicius
elif operacija == "*":
    rezultatas = pirmas_skaicius * antras_skaicius
else:
    rezultatas = f"Neatpazinta operacija {operacija}" 


print(rezultatas)

