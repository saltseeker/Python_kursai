#def laipsniu(skacius=0, laipsnis): ###Blogai
def laipsniu(skaicius, laipsnis):
    return skaicius ** laipsnis

#print("Keliam dvejeta ketvirtuoju:", laipsniu(2, 4))
#print("Penki kvadratu:", laipsniu(5))
#print("Trys kubu", laipsniu(skaicius=3, laipsnis=3))
#print("du kvadratu", laipsniu())
#print("Penktuoju desimt: ", laipsniu(laipsnis=5, skaicius=10))
#print("du septintuoju:", laipsniu(laipsnis=7))
arg1 = int(input("Iveskite skaiciu: "))
arg2 = int(input("Iveskite laipsni: "))
rezultatas = laipsniu(arg1, arg2)
print(f"{arg1} pakeltas {arg2} = {rezultatas}")
#print(f"{arg1} pakeltas {arg2} = {laipsniu(arg1, arg2)}") ##2 varijantas