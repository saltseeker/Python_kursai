# Parašyti programą, kuri:

# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)


from datetime import date, timedelta, datetime
 

now = datetime.now()
before_5_days = now - timedelta(days=5)
now_8 = now + timedelta(hours=8)
formated_date = now_8.strftime("%Y-%m-%d %I:%M:%S")
formated_now = now.strftime("%Y %m %d, %I:%M:%S")





print("Dabar yra: ", now, "data")
print("Before 5 days: ", before_5_days)
print(formated_date)
print(formated_now)

