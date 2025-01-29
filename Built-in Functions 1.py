#---- all() + any() + bin() + id() ----#

# all(iterable)

# x=[1,2,3,4,6,5]
x=[[],2,3,4,6,5]

if all(x):
    print("All Elements are true !")
else:
    print("There is at least One Element Is False !")


# any(iterable)

y=[0,0,[]]

if any(y):
    print("There is at least one element is true !")
else:
    print("All Elements are False !")

# bin(number)
# bin() ==>> print Binary Numbers (Transform to Machine Language)
# print(bin("Ahmed")) TypeError: 'str' object cannot be interpreted as an integer

print(bin(123)) # 0b1111011

# id(variable)
# Return The Address Of The Variable

a=1
b=2

print(id(a)) # 140735361770280
print(id(b)) # 140735361770312