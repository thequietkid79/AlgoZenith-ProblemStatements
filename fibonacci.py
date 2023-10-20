# take input from the user
n = int(input("Enter the number of terms: "))

# define the fibonacci function which prints the Fibonacci series up to n terms
def fibonacci(n):
    # initialize variables
    a, b = 0, 1
    count = 0

    # check if the number of terms is valid
    if n < 0:
        print("Please enter a positive integer")
    elif n == 0:
        print("Fibonacci sequence upto",n,":",a)
    elif n == 1:
        print("Fibonacci sequence upto",n,":",b)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a)
            c = a + b
            # update values
            a = b
            b = c
            count += 1

# print the output using the fibonacci function
fibonacci(n)
