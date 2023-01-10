cars = [
    {"Gamintojas": "Tesla", "modelis": "Model Y", "Metai": 2022, "spalva": "Baltas"},
    {"Gamintojas": "Tesla_2", "modelis": "Model X", "Metai": 2017, "Spalva": "Juodas"},
    {"Gamintojas": "Honda", "modelis": "Odyssey", "Metai": 2001, "Variklis": "V6-3500", "Spalva": "Titanium Dark Grey"},
    {"Gamintojas": "Arklys", "modelis": "Greitas", "Metai": 2018, "Vardas": "Žaibas", "Spalva": "Juodas"},
    {"Gamintojas": "Opel", "modelis": "Astra", "Metai": 1997}
]

def automobilis(Gamintojas, modelis, Metai, **kwargs):
    print(f"Gamintojas: {Gamintojas}")
    print(f"Modelis: {modelis}")
    print(f"Metai: {Metai}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def choose_car():
    while True:
        print("Pasirinkite automobili: ")
        for i, car in enumerate(cars):
            print(f"{i+1}. {car['Gamintojas']} ")
        choice = input()
        if choice == "x":
            break
        chosen_car = cars[int(choice) - 1]
        automobilis(**chosen_car)

choose_car()
