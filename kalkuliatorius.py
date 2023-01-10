while True:
    try:
        skaicius = int(input("Iveskite skaiciu: "))
    except ValueError:
        print("Ivestas ne skaicius, bandykite dar")
    else:
        break
print (f"Iveskite skaicus: {skaicius}")        
