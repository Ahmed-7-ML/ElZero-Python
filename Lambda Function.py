# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Ex1:Add 10 to argument a, and return the result:

x = lambda a : a + 10

print(x(4)) # 4 + 10 = 14

# Ex2:Multiply argument a with argument b and return the result:

y = lambda a , b : a * b

mul = y(5,2)

if mul > 10 :
    mul = mul / 20
else: # mul <= 10
    mul = 0

print(mul)

# Ex3:Summarize argument a, b, and c and return the result:

z = lambda a , b , c : a + b + c

sum = z(10,20,39)

if(sum % 2 ==0): # Even
    print("Even")
else:
    print("Odd")

# Ex4:Lambda Inside a Function
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Ex5:Show_Name

def Show_Name():
    return lambda name : name

My_Name=Show_Name()
print(My_Name("Ahmed"))


print(Show_Name.__name__)
print(My_Name.__name__) # Anonmous

print(type(Show_Name()))
print(type(My_Name))