
def print_car_info(**kwargs):
  print(f"Gamintojas: {kwargs['Gamintojas']}")
  print(f"Modelis: {kwargs['modelis']}")
  print(f"Metai: {kwargs['metai']}")
  for key, value in kwargs.items():
    if key not in ["Gamintojas", "modelis", "metai"]:
      print(f"{key}: {value}")


car_info1 = {
  "Gamintojas": "Tesla",
  "modelis": "Model Y",
  "metai": 2022,
  "spalva": "Baltas"
}
print_car_info(**car_info1)

car_info2 = {
  "Gamintojas": "Tesla",
  "modelis": "Model X",
  "metai": 2017,
  "spalva": "Juodas",
  "kablys": True
}
print_car_info(**car_info2)

car_info3 = {
  "Gamintojas": "Honda",
  "modelis": "Odyssey",
  "metai": 2001,
  "variklis": "V6-3500",
  "spalva": "Titanium Dark Grey"
}
print_car_info(**car_info3)

car_info4 = {
  "Gamintojas": "Arklys",
  "modelis": "Greitas",
  "metai": 2018,
  "Vardas": "Žaibas",
  "spalva": "Juodas"
}
print_car_info(**car_info4)

car_info5 = {
  "Gamintojas": "Opel",
  "modelis": "Astra",
  "metai": 1997
}
print_car_info(**car_info5)