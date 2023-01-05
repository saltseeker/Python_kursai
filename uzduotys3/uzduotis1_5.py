

#Gražintų sąrašą tik su nepasikartojančiais paduoto sąrašo elementais.



def info_apie_sakini(stringas):
    print(f"sakinyje yra {len(stringas.split())} zodziu")
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    print(f"didziosios: {didziosios}, mazosios: {mazosios}, skaiciai: {skaiciai}")

info_apie_sakini("Tiek raidziau ir skacius 1323")