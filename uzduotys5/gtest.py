
from datetime import datetime

eilerastis = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


def atvirksciai(sakinys):
    return sakinys[::-1]


def patikrinti_sakini(sakinys):
    print("Žodžių kiekis:", len(sakinys.split()))
    print("Skaičių kiekis:", sum(c.isdigit() for c in sakinys))
    print("Didžiųjų raidžių:", sum(c.isupper() for c in sakinys))
    print("Mažųjų raidžių:", sum(c.islower() for c in sakinys))

def didziosiomis(sakinys):
    return sakinys.upper()


# 1 Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.

with open('tekstas1.txt', 'w') as failas:
    failas.write(eilerastis)

# 2 Atspausdintų tekstą iš sukurto failo

with open('tekstas1.txt', "r") as failas:      
    tekstas = failas.read()
print(tekstas)    

# 3 Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką

with open("tekstas1.txt", "a") as failas:
    failas.write('\n')
    failas.write(str(datetime.today()))

# 4 Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
 

with open("tekstas1.txt", "r") as failas:
    lines = failas.readlines()

for eilute, line in enumerate(lines):
    lines[eilute] = str(eilute+1) + " " + line

with open("tekstas1.txt", "w") as failas:
    failas.writelines(lines)


# 5 Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."

keiciam = ""

with open('tekstas1.txt', 'r') as failas:
    keiciam = failas.read()

keiciam = keiciam.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

with open('tekstas1.txt', 'w', encoding="UTF-8") as failas:
    failas.write(keiciam)


# 6 Atspausdintų visą failo tekstą atbulai:

with open('tekstas1.txt', 'r') as failas:
    print(atvirksciai(failas.read()))

# 7 Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

with open('tekstas1.txt', 'r') as failas:
    print(patikrinti_sakini(failas.read()))

# 8 Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS:

with open('tekstas1.txt', 'r', encoding="UTF-8") as nuskaitomas_failas:
    with open('tekstas_didziosiomis.txt', "w", encoding="UTF-8") as irasomas_failas:
        irasomas_failas.write(didziosiomis(nuskaitomas_failas.read()))
