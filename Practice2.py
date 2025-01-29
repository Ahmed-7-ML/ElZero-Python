#                        Exercise 2: Handling ValueError                          #
# Imagine you have a number and want to calculate its square root. 
# To do this, you need to create a Python function.
# You give this function one number, 'number1'.

# The function should generate the square root value 
# if you provide a positive integer or float value as input.
# However, the function should be clever enough to detect the mistake 
#  if you enter a negative value. It should kindly inform you with a message saying,
# 'Invalid input! Please enter a positive integer or a float value.

from math import sqrt
def Square_Root(number1):
    try:
        if(number1 >= 0):
            #return pow(number1 ,0.5)
            return sqrt(number1)
    except ValueError:
        print('Invalid input! Please enter a positive integer or a float value')


n = float(input("Enter The Number: "))
print(f"The Square Root of {n} is {Square_Root(n)}")