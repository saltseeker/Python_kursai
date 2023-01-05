import datetime



data = datetime.datetime.strptime(f"{metai}-{menuo}-{diena}", "%Y-%m-%d")
print(type(data))
print(f"ivesta data: {data.date()}")
siandien = datetime.date.today()
print(f"siandien: {siandien}")
amzius = siandien - data.date()
print(f"nuo ivestos datos praejo {amzius.days} dienu")
