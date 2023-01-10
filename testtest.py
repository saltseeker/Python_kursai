calculation_to_unitis = 24
name_of_unit = "hours"







def days_to_unitis(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_unitis} {name_of_unit}")


user_input = input("Enter the number: ")

if user_input.isdigit():
    user_num = int(user_input)
    days_to_unitis(user_num)
else:
    print("no")

