# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random

# Generate two random numbers between 1 and 100
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Display the addition question
print(f"What is {num1} + {num2}?")

# Prompt the user for their answer
user_answer = int(input("Enter your answer: "))

# Calculate the correct answer
correct_answer = num1 + num2

# Check if the user's answer is correct and display a message
if user_answer == correct_answer:
    print("Correct! Well done!")
else:
    print(f"Incorrect. The correct answer is {correct_answer}.")