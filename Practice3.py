#                    Exercise 3: Handling Generic Exceptions                    #
# Imagine you have a number and want to perform a complex mathematical task.
# The calculation requires dividing the value of the input argument 
# "num" by the difference between "num" and 5, and the result has to
# be stored in a variable called "result".

# You have to define a function so that it can perform that complex mathematical task.
# The function should handle any potential errors that occur during the calculation.
# To do this, you can use a try-except block. 
# If any exception arises during the calculation,
# it should catch the error using the generic exception class "Exception" as "e". 
# When an exception occurs,
#  the function should display "An error occurred during calculation.

def ComplexTask(num):
    try:
        result = num /(num - 5)
    except Exception as e :
        print("An error occurred during calculation")
    else:
        print("The Final Result", result) 

num = int(input("Enter a number: "))
ComplexTask(num)

