cars = [
    {"Gamintojas": "Tesla", "modelis": "Model Y", "Metai": 2022, "spalva": "Baltas"},
    {"Gamintojas": "Tesla_2", "modelis": "Model X", "Metai": 2017, "Spalva": "Juodas"},
    {"Gamintojas": "Honda", "modelis": "Odyssey", "Metai": 2001, "Variklis": "V6-3500", "Spalva": "Titanium Dark Grey"},
    {"Gamintojas": "Arklys", "modelis": "Greitas", "Metai": 2018, "Vardas": "Žaibas", "Spalva": "Juodas"},
    {"Gamintojas": "Opel", "modelis": "Astra", "Metai": 1997}
]

def automobilis(Gamintojas, modelis, Metai, **kwargs):
    print("------------------")
    print(f"Gamintojas: {Gamintojas}")
    print(f"Modelis: {modelis}")
    print(f"Metai: {Metai}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        

def choose_car():
    while True:
        print("------------------")
        print("Pasirinkite automobili: ")
        for i, car in enumerate(cars):
            print(f"{i+1}. {car['Gamintojas']} ")
        print("------------------")
        print("Noredami iseiti iveskite'x'") 
        print("------------------")   
        choice = input()
        if choice == "x":
            break
        try:
            chosen_car = cars[int(choice) - 1]
        except (ValueError, IndexError):
            print("------------------")
            print("Prasome ivesti teisinga pasirinkima.")
            print("------------------")
            continue
        automobilis(**chosen_car)

choose_car()

