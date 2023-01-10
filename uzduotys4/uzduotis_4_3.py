# Parašyti programą, kuri:

# Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# Metų
# Mėnesių
# Dienų
# Valandų
# Minučių
# Sekundžių
# Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, .days, .total_seconds()

# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):






from datetime import datetime



user = input("Iveskite data ir laika tokiu formatu yyyy-mm-dd hh:mm:ss : ")

try:
    datetime_object = datetime.strptime(user, '%Y-%m-%d %H:%M:%S')
except ValueError:
    raise Exception("Neteisingai ivestas formatas") 
   

current_date = datetime.now()
skirtumas = current_date - datetime_object 
years = skirtumas.days // 365 
months = skirtumas.days // 30
hours = skirtumas.days * 24
minutes = skirtumas.days * 24 * 60




print(datetime_object)
print(skirtumas)
print(years, months, skirtumas.days, hours, minutes, round(skirtumas.total_seconds()))
print(f"Kiek praejo: \nmetu {years}, \nmenesiu: {months}, \ndienu: {skirtumas.days}, \nvalandu: {hours}, minuciu: {minutes}: sekundziu: {round(skirtumas.total_seconds())} ")