import calendar


def ar_keliamieji(metai):
    return calendar.isleap(metai)


print(ar_keliamieji(2020))
print(ar_keliamieji(2100))
print(ar_keliamieji(2000))