# Take input from the user
num = int(input("Enter a number: "))

#define the is_palindrome function which checks whether or not a function is palindrome or not
def is_palindrome(num):
    # Convert the num integer to a string
    num_str = str(num)
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Check if the original string and the reversed string are equal
    if num_str == reversed_str:
        return True
    else:
        return False

# Test whether or not the user input is palindrome using the is_palindrome function and print the output
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
