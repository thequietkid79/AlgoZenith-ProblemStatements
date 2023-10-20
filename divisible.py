# Prompt the user for an input for an integer
number = int(input("Enter a number: "))

# Define a function to check whether or not the number is divisible by 2 or 3
def checkdiv(number):
    if number % 2 == 0 and number % 3 == 0:
        print("The number is divisible by both 2 and 3.")
    elif number % 2 == 0 and number % 3 != 0:
        print("The number is divisible by 2 but not by 3.")
    elif number % 2 != 0 and number % 3 == 0:
        print("The number is divisible by 3 but not by 2.")
    else:
        print("The number is divisible by neither 2 nor 3.")

# Print the output using the checkdiv function
checkdiv(number)
