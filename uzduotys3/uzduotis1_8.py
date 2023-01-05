#Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

def nuo_galo(sakinys):
    zodziai = sakinys.split()[::-1]
    return zodziai


print(nuo_galo("sakinys nuo galo"))