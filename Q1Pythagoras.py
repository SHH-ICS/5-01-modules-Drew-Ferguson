# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math

# Prompt the user for the lengths of the two legs
a = float(input("Enter the length of leg a: "))
b = float(input("Enter the length of leg b: "))

# Calculate the length of the hypotenuse
c = math.sqrt(a**2 + b**2)

# Display the result
print(f"The length of the hypotenuse is: {c:.2f}")