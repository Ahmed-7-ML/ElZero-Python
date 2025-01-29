# U Can Write Quotations(Single / Double) or not

tuple1=("Ahmed","Akram")
tuple2="Ahmed","Akram"

print(tuple1)
print(tuple2)

print(type(tuple1))
print(type(tuple2))

#Difference Between String and Tuple

tuple3=("Ahmed",)
tuple4="Ahmed",
#U Must Put Comma In Case Of One Element In Tuple
# U Must Put Comma " , " In Case Of Removing Paranthesis 

string1="Ahmed"
string2=("Ahmed")

print(tuple3)
print(tuple4)
print(string1)
print(string2)

print(type(tuple3))
print(type(tuple4))
print(type(string1))
print(type(string2))

print(len(tuple3))
print(len(tuple4))

#Tuple Indexing

# Can Have Data Of Different Data Types
# Can Have Duplicate Members
tuple5=("Ahmed",1,10.67,"Ahmed",1,10.67,True,False)

print(tuple5[0])
print(tuple5[1])
print(tuple5[2])
print(tuple5[-2])
print(tuple5[-3])
print(tuple5[-1])

#Tuple Slicing
#End Not Included
print(tuple5[0:3])
print(tuple5[0:3:1])
print(tuple5[0:3:2])

#Tuple is Immutable

# tuple5[0]="One"
# print(tuple5) typeError: 'tuple' object does not support item assignment


# sorted Function =>> Sort The Tuple That Have Numbers ,Alphabetic(Capital / Small)
t1=(1,5,7,9,3,2,69,0)

t2=sorted(t1)

print(t2)

t1=('A','Z','Y','D')

t2=sorted(t1)

print(t2)

t1=('a','z','y','d')

t2=sorted(t1)

print(t2)

t1=('A','Z','Y','d')

t2=sorted(t1)

print(t2)



