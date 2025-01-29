# tuple concatenation

tuple1=(1,2,3); tuple2=(4,5,6,7)
tuple3=tuple1+tuple2

print(tuple1)
print(tuple2)
print(tuple3)

tuple4=tuple1+("Ahmed",)+tuple2
print(tuple4)

# tuple5=tuple1+("Ahmed")+tuple2
# print(tuple5) TypeError: can only concatenate tuple (not "str") to tuple
# ("Ahmed") => String BUT ("Ahmed",) => Tuple


#Tuple , List ,String With Repeat Operator (*)

str1="Ahmed"
lst1=["A","h","m"]
tup1=("Amr","Ali")

print(str1*3)
print(lst1*3)
print(tup1*3)

#Methods

#1-count() =>Return The Number Of Occurence Of an Element / a Value

tup2=(1,2,3,1,2,3,2,4,3,3,2)

print(tup2.count(1))
print(tup2.count(3))
print(tup2.count(4))
print(tup2.count(2))
print(tup2.count("Ahm"))

print("@"*40) #Separator

#2-index() => Return The (((((((First))))))) Index Of The Element If Founded
#2-index() => Return Error If Not Found

tup3=("DD",12,True,False,"AA",12,True)

print(tup3.index("DD"))
print(tup3.index(12))
print(tup3.index(True))

#Formatting
print("The Index of 12 is :%d"%tup3.index(12))
print("The Index of 12 is :{}".format(tup3.index(12)))
print(f"The Index of 12 is :{tup3.index(12)}")

#Tuple Destruct

a=("A","B","C")
x,y,z="A","B","C"

print(x)
print(y)
print(z)

X,Y,Z=a
print(X)
print(Y)
print(Z)

b=("II","I",4,5)

s,r,_,t=b
# _ =>Ignore (4)
print(s)
print(r)
print(t)