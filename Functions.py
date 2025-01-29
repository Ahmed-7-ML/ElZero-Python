# Function => Block Of Code Which Runs When Calling It
# def Function_Name(Arguments) : => Defination Of A Function
# Then Body => The Executable Code When Calling
# def => KeyWord To Define a Function

# Arguments => Arbitary , Keyword , Aribtary Keyword


# Without Arguments
def First_Function(): # Defination 
    print("We did it") # Code Body Of The Function 


First_Function()  # Calling 

# With One Argument
def number_squared(number): # Defination 
    print(number**2) # Code Body Of The Function

number_squared(3) # Calling
# number_squared() #TypeError: number_squared() missing 1 required positional argument: 'number'


# With Multible Arguments
def number_squared_cust(number,power): 
    print(number**power)

number_squared_cust(5,3)


# BMI Calculator 
def BMI_Calc(weight,height):
    BMI=(weight*703)/(height*height)


weight=int(input("Enter Your Weight In Bounds : "))
height=int(input("Enter Your Height In Inches : "))

BMI=BMI_Calc(weight,height)
print(BMI)












