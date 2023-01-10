import datetime


start_date = datetime.date(1955, 6, 23)
end_date = datetime.date(2021, 1, 1)


birthday_weekday = 4
count = 0

date = start_date
while date < end_date:
    if date.weekday() == birthday_weekday and date.month in [4, 6, 9, 11]:
        count += 1
    elif date.weekday() == birthday_weekday:
        count += 1
date += datetime.timedelta(days=1)
    


print(count)