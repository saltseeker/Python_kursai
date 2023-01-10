class kate:
    vardas = ""
    spalva = ""    # nereikia jei __init__ nurodita || Self yra privaloma kiekvienam
    kojos = 0          #statines reiksmes
    amzius = 0

    def __init__(self, vardas, spalva="Juoda", kojos=4) -> None:   # ->None   nurodo koki funkcijo kintamaji grazins, nebutinas siou atveju
        self.spalva = spalva                               #init paima is funkcijos ne is klases
        self.kojos = kojos                                   #standartines reiksmes, galima keisti kitose eilutese
        self.vardas = vardas                                 #dinamines reiksmes
        self.anzius = 0

    def miaukseti(self):
        print("miau")

    def _judinti_kojas(self, kaip=""):                                 # __ vidines funkcijos
        return kaip

    def _ziureti(self, kur="tiesiai"):
        return kur

    def begti(self, kryptis="tiesiai", judesys=""):
        kaip = self._judinti_kojas(judesys)
        kur = self._ziureti(kryptis)
        if kaip:
            print(f"begu {kaip} {kur}")
        else:
            print(f"begu {kur}")
    
    def susilauzyti_koja(self, kiek=1):
        self.kojos -= kiek

    def sugydyti_koja(self, kiek=1):
        self.kojos += kiek

    def __str__(self) -> str:
        return f"vardas: {self.vardas}, spalva: {self.spalva}, kojos: {self.kojos}, amzius: {self.amzius}"    # sukuri stringa. iskvieti su objektu siuo atveju "miauklius"

    def __repr__(self) -> str:
        return f"({self.vardas}, {self.spalva}, {self.kojos})"


kates = []
while True:
    print("===MENU===")
    print("1. Prideti kate")
    print("2. Rodyti kate")
    print("9. palaidoti kate")
    print("0. Padeti rageli")
    try:
        pasirinkimas = int(input("pasirinkite: "))
    except ValueError:
        print("blogas pasirinkimas") 
    else:
        if pasirinkimas == 0:
            break
        if pasirinkimas == 1:
            try:
                nauja = kate(
                    input("vardas: "),
                    input("Spalva: ") or "juodas",
                    int(input("kojos: ")) or 4,
            )
            except ValueError:
                print("Klaida: kojos turi buti skaicius")
            else:
                kates.append(nauja)
                print(f"Gime nauja kate {nauja}")
        if pasirinkimas == 2:
            if len(kates):
                for id, kate in enumerate(kates):                                  # enumerate duoda indexa netik reiksme | ideda  eiles numeri | siuo atveju sunumeruoja kates
                    print(f"ID: {id}, {kates}")
                else:
                    print('kolkas kaciu nera...')    
        if pasirinkimas == 9:
            try:
                id = int(input("Iveskite kates ID, kuria trinam"))
                palaidota = kates.pop(id)                 # ka ismetei ta grazini i kintamaji
            except ValueError:
                print("klaida: IDturi but skaicius")
            except IndexError:
                print("Klaida: Kate su tokiu ID neegzistuoja")
            else:
                print(f"Kate {palaidota} buvo paliadota")        