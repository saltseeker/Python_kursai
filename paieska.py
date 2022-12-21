sakinys = "Studentai sekimingai mokesi su python ieskoti tekste slieku..."

ieskom = input("ko ieskom?: ")

for raide in sakinys:
    if ieskom == raide:
        print("radom!")
        break
else:
    print("neradom {ieskom}.")    