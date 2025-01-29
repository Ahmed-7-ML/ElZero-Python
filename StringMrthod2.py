#String Methods 2

#1-split()

d="I Love Python PhP and MySql"
print(d.split())
d="I-Love-Python-PhP-and-MySql"
print(d.split("-"))
print(d.split())

#split(Separator,MaxSplit)
a="I-Love-Python-PhP-and-MySql"
print(a.split("-",2))
print(a.split("-",3))

#2-rsplit()
print(a.rsplit("-",3))

#Usage of " in " KeyWord
a="Ahmed Akram"
print("hm"in a) # will return True or False
print("Hm"in a) 
print(" "in a) 
print("Ahmed"in a) 

if("Ahmed"in a):
    print("True")

print(type("Ahmed"in a)) # This Type is bool that return True or False

#Usage of "not in" KeyWord
b="Kamel Amer"
print("Ka" not in b) # if not in return True , otherwise return False 
print("KA" not in b) 

if("Ar" not in b):
    print("True It is not in a string")

#replace() -->>Built-in functions: replace
c="Python awesome!"
print(c.replace("Python","C++"))
d="Ahmed Akram"
print(d.replace('A','K'))
#if character is repeated ,will remove all of it

#Usage of Format Function by aid of {} to Place Number in The Right Place
Age=20
print("I am Ahmed Akram , I am {} ".format(Age))

price=40
numbers=5
product=567
print("I bought {0} with {1} numbers with price {2}".format(product,numbers,price))

#\000 usage of Octal Value Same As \xhh Hex Value
print("\123\110\101\111\115\101\101 \115\117\110\101\115\115\105\104")
#\f -->>Form Feed
print("\fAhmed\fAkram\f")

#expandtabs()
f="Ahmed\tAkram\tWith\tZeyad\tAkram"
print(f.expandtabs(3)) #Control The Number Of Spaces

#To Check String is....
one="I Love Python And 3D"
two="I Love Python And 3d"
# istitle()-->>Check if the string is title or not
print(one.istitle())
print(two.istitle())

three=" "
four=""
#isspace()-->> Check if the string cotain spaces or not
print(three.isspace())
print(four.isspace())

five="ahmed akram"
fiveMod="Ahmed Akram"
#islower()-->>Check if all characters is in LowerCase or not
print(five.islower())
print(fiveMod.islower())
six="AHMED AKRAM"
sixMod="AHmeD AkraM"
#isupper()-->>Check if all characters is in UpperCase or not
print(six.isupper())
print(sixMod.isupper())

