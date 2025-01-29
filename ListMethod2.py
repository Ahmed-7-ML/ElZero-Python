# claer() ,copy(), count(), index(), insert(), pop()

#Clear()
a=[1,2,3,4,5,"A",'A']
a.clear()
print(a) # []

#Copy()
c=[1,"adj",2.5]
b=c.copy()
print(b)
# c-->>Main List , b-->>Copied List
c.append("Ahmed")
print(c); print(b)

#Count()
z=[1,3,2,34,1,1,3,1,22]
print(z.count(1))

#Index()
index=z.index(34)
print(index)

#Insert(index,object)
z.insert(2,"Before index=2")
print(z)
z.insert(-1,"Before index=-1")
print(z)

z=[1,3,5,6,2,88,0,"A"]
#pop(index)
print(z.pop()) #Default Remove and Retuen The Last Index
print(z.pop()) # Like a Stack
print(z)
print(z.pop(0))
print(z.pop(-1))
print(z)