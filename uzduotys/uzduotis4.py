a = float(input("Iveskite pirma skaiciu: "))
b = float(input("Iveskite antra skaiciu: "))
veiksmas = input("Koki matematini veiksma atlikti (/ - + *): ")
if veiksmas == "/":
    print('Lygu:', a / b)
if veiksmas == "-":
    print('Lygu:', a - b)
if veiksmas == "+":
    print('Lygu:', a + b)
if veiksmas == "*":
    print('Lygu:', a * b)

print("skaiciuotuvas")

a = int(input("Iveskite pirma skaiciu: "))
b = int(input("Iveskite antra skaiciu: "))
veiksmas = (input("Koki veiksma atlikti: (+ - / * ): "))
if  veiksmas == "+":
   print("jusu atsakymas:", a + b)
if veiksmas == "-":
   print("jusu atsakymas:", a - b)
if veiksmas == "/":
   print("jusu atsakymas:", a / b)
if veiksmas == "*":
   print("jusu atsakymas:", a * b)