# Based on user input, program recommends a method of travel.

howFar = int(input("How many miles do you want to travel? "))

# if howFar < 3:
#     print("You should walk.")
# elif howFar < 300:
#     print("You should drive.")
# else: 
#     print("You should fly.")

# improved version that employs the format method

if howFar < 3:
    method_of_travel = "walk"
elif howFar < 300:
    method_of_travel = "drive"
else: 
    method_of_travel = "fly"

print("You should " + method_of_travel + ".")

# print("You should {}.".format(method_of_travel))