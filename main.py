import random
import os

print("\nThis is my first python app! its basicly a calculator so i can practice python.")

def numberInput():

    while True:
        number = input('Please enter a value:')

        try:
            return int(number)
        except ValueError:
            print("Error! this is not a number!")


finalMath = numberInput()
mathString = "" + str(finalMath)
keepAsking = True
shouldIKeepAsking = "Y"

while keepAsking:
    if shouldIKeepAsking == "Y" or shouldIKeepAsking == "y":
        print("\nAllright! what action would you like to do?(Addition/Subtraction/Multiplication/Division)")
        action = input("enter your action: ")
        value = numberInput()

        if action == "Addition" or action == "addition" or action == "+":
            finalMath += value
            mathString += " + " + str(value)
        elif action == "Subtraction" or action == "subtraction" or action == "-":
            finalMath = finalMath - value
            mathString += " - " + str(value)
        elif action == "Multiplication" or action == "multiplication" or action == "*":
            finalMath = finalMath*value
            mathString += " * " + str(value)
        elif action == "Division" or action == "division" or action == "/":
            finalMath = finalMath/value
            mathString += " / " + str(value)
        else:
            print("\nLooks like you entered some invalid input. Please try again")

        print("result: ", finalMath)
        shouldIKeepAsking = input("\nWould you like to continue your calculation? Y/N")
    elif shouldIKeepAsking == "N" or shouldIKeepAsking == "n":
        keepAsking = False
    else:
        shouldIKeepAsking = input("\nWould you like to continue your calculation? Y/N")


mathString += " = " + str(finalMath)
print("final result: " + mathString)
