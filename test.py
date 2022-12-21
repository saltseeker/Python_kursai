#print(f"Minutes in 20 days is: {20 * 24 * 60}")

# print(f"20 days are {50} minutes")


# print(f"In 20 days there is {20 * 24 * 60 * 60} seconds")
# print(f"In 40 days there is {40 * 24 * 60 * 60} seconds")
# print(f"In 100 days there is {100 * 24 * 60 * 60} seconds")
# print(f"In 60 days there is {60 * 24 * 60 * 60} seconds")


calculation_to_units = 24 
name_of_unit = "hours"

def days_to_units(num_of_days, custome_message):
     print(f" {num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}")
     print(custome_message)



days_to_units(20, "Awesome!")
days_to_units(25, "Looks good")





# print(f"In 20 days there is {20 * calculation_to_units} {name_of_unit}")
# print(f"In 40 days there is {40 * calculation_to_units} {name_of_unit}")
# print(f"In 100 days there is {100 * calculation_to_units} {name_of_unit}")
# print(f"In 60 days there is {60 * calculation_to_units} {name_of_unit}")