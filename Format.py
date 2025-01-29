#Format By Old Way
#%s-->>String 
#%d-->>Integer
#%f-->>Floating Point Number

#To Control Floating Point -->> By %._f 
#To Truncate String -->> By %._s 

str1="Ahmed"
age1=20
rank=10

print("My Name Is %s"%str1)
print("My Age Is %s"%age1)
print("My Rank Is %s"%rank)
print("I am %.5s and My Age is %d and My Rank is %.3f" %( str1 ,age1 , rank ))

#Format By New Way
#{:s}-->>String
#{:d}-->>Integer Number
#{:f}-->>Floating Point Number
#Using ".format(-,-,-,...)"
str1="Ahmed"
age1=20
rank=10

print("I am {}".format(str1))
print("I am {} Years Old".format(age1))
print("My Rank Is {}".format(rank))
print("I am {} , I am {} Years Old And My Rank Is {}".format(str1,age1,rank))
print("I am {:s} ,I am {:d} Years Old And My Rank Is {:f}".format(str1,age1,rank))

#To ConTrol Floating Point By {:._f}
print("I am {:s} , I am {:d} Years Old And My Rank Is {:.2f}".format(str1,age1,rank))

#Truncate String By {:_s}
name="Hello Ahmed Amer"
print("My Message is {}".format(name))
print("My Message is {:s}".format(name))
print("My Message is {:.11s}".format(name))

# Foramtting Numbers
#{:"Char That I Want To Put Between Numbers" d}
salary=2000
print("My Salary Is {}".format(salary))
print("My Salary Is {:d}".format(salary))
print("My Salary Is {:_d}".format(salary))
print("My Salary Is {:,d}".format(salary))

#ReArranging Items (String,Numbers)

#Data-->>Objects: Zero-Based Indexing In Python

#Examble
a,b,c="Ahmed","Akram","Zeyad"
print("Hello {} {} {}".format(a,b,c)) #a-->>0 ,b-->>1,c-->>2
print("Hello {1} {2} {0}".format(a,b,c))

x,y,z=10,20,30
print("Numbers : {} {} {}".format(x,y,z)) #x-->>0 ,y-->>1,z-->>2
print("Numbers : {2} {1} {0}".format(x,y,z))
print("Numbers : {2:d} {1:d} {0:d}".format(x,y,z))
print("Numbers : {2:.2f} {1:.3f} {0:.4f}".format(x,y,z))

#Anthor Wonderful Way For Formatting
print(f"Numbers : {x} {y} {z}")
