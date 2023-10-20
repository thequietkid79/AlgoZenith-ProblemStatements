# Define a variable for the number of rows in the pattern, here it's 5.
n = 5

# Define a function that takes an integer n and prints a pattern
def pypattern(n):
    # define the number of rows in the pattern
    for i in range(0, n):
        # define the number of stars to print on each row of the pattern
        for j in range(0, i+1):
            # print stars and end the line after each row
            print("* ",end="")
        # ending line after each row to make different rows for the pattern
        print("\r")
 
# Print the final pattern
pypattern(n)
