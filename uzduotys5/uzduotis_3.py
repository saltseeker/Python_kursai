

multi_inputs = ""

while True:
    user_input = input("Iveskite: ")
    multi_inputs += user_input  + "\n"  #concatinate multiple user inputs with line breaks
    if not user_input:
        break
    

failo_pav = input("Iveskite failo pavadinima: ")


with open (f'{failo_pav}.txt', "w") as file:
    file.write(multi_inputs)

    

 
