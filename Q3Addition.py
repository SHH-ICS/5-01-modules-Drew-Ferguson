# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print(f"What is {num1} + {num2}?")

user_answer = int(input("Enter your answer: "))

correct_answer = num1 + num2

if user_answer == correct_answer:
    print("Correct! Well done!")
else:
    print(f"Incorrect. The correct answer is {correct_answer}.")