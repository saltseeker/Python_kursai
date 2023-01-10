#tikrina ar ivede skaiciu

skaicius = int(input("iveskite skaiciu: "))

try:
    tiesa = int(skaicius) > 0
except Exception as error:
    print("klaida!", error)
else:
    print(f"{tiesa} yra daugiau uz 0: {tiesa}")    