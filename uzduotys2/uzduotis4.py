
import random

num = None

print("welcome to the lottery")
print("To win you must not to roll number 5")


veiksmas = input("Are you read (yes, no)?: ")
if veiksmas == "no":
     print("Sad, maybe next time")
     
if veiksmas == "yes":
     print("Good luck") 
     num = random.randint(1, 6)
     print("Your number is")
     print(num)


     if num and num == 5:
          print("you lost, better luck next notime ")
     else:
          print("you won!")
          