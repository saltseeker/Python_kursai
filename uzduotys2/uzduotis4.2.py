skaitliukas = 0
import random  
while True:
    skaicius = random.randint (1, 6)
    print(skaicius)
    skaitliukas += 1
    if skaicius == 5:
        print("Pralaimejai")
        break
    if skaicius==3:
        print("laimejai")
        break