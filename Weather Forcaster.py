"""1. Exceptional Weather Forecast
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested."""

import math

def temperature_converter(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        rounded_celsius = round(celsius, 2)
        return rounded_celsius

while True:
    try:
        fahrenheit_input = int(input("Enter a temperature in Fahrenheit: "))
        converted_temp = temperature_converter(fahrenheit_input)
    except ValueError:
        print("\nPlease enter the temperature in digits.\n")
        continue
    else:
        print(f"\n{fahrenheit_input} degrees Fahrenheit is {converted_temp} degrees Celsius.")
    finally:
        print("Thank you for using the exceptional weather forcaster!\n")

    continue_input = input("Would you like to convert another temperature in Fahrenheit to Celsius? (yes/no): ").lower()
    if continue_input != 'yes':
        break
