#from modules import testinis                             ##1 varijantas

tekstas = "labas rytas"
# print(testinis.atbulai(testinis.kintamasis))            ##1 varijantas
# print(testinis.atbulai(tekstas))                        ##1 varijantas

#from modules.testinis import atbulai, kintamasis        ##2 varijantas   
from modules.testinis import *


print(atbulai(tekstas))                                 ##2 varijantas
print(atbulai(kintamasis))                              ##2 varijantas

from kiti_zaislai import geris
print(geris.geras)




# from modules import testinis as funkcijos
# from modules.testinis import kintamasis as tk                  # pervadinom


# print(funkcijos.atbulai(tekstas))
# print(funkcijos.atbulai(tk))