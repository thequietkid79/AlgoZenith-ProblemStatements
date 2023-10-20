# loop through the numbers 1 to 100
for num in range(1, 101):
    # define that the num variable is greater than 1 as prime numbers need to be greater than 1
    if num > 1:
        # check if the number is divisible by any number from 2 to itself-1
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            # if the number is not divisible by any number from 2 to itself-1, print it as it must be a prime number
            print(num)