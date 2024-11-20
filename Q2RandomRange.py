# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.

import random

start = float(input("Enter the starting number of the range: "))
end = float(input("Enter the ending number of the range: "))

random_number = random.uniform(start, end)

print(f"A random number between {start} and {end} is: {random_number:.2f}")