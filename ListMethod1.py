# append() ,extend(),remove(),reverse(),sort(reverse=True or False)

#append()-->>Add New Item
MyFriends=["Yousef","Amaar","Karoup"]
MyFriends.append("Ayman")
MyFriends.append("Zeyad")
MyFriends.append(100)
MyFriends.append(True)
MyFriends.append(10.6746)
print(MyFriends)

MyOldFriends=["Heshame",'Salma',"Aya"]
MyFriends.append(MyOldFriends) # Can Add Any Types and List
print(MyFriends)
# Add List As A One Element
# Can Access The Item Inside Second List That Inside First List
print(MyFriends[-1][0])
print(MyFriends[8][1])
print(MyFriends[-1][2])


print("="*100)


#extend() -->>Add The List Not As A One Element But into Elements
a=[1,2,3,4]
b=["A","B","C"]
c=[True,False]

a.extend(b)
a.extend(c)
print(a)

#The extend() method does not have to append lists,
#you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print("="*100)

#remove()-->>delete The Item From The List
a=[1,2,"A",'B',"A",1]
a.remove("A")
print(a)
a.remove(1)
print(a)

#Sort()-->>Rearrange The Elements (Numbers Only OR Characters Only )
y=[-1,100,3734,5,2,4,7,4]
y.sort() # By Default Sort Ascending
print(y)
y.sort(reverse=False) # Sort Ascending
print(y)
y.sort(reverse=True) # Sort DeAscending
print(y)

y=["A",'b',"C",'z',"D",'f']
y.sort() # By Default Sort Ascending
print(y)
y.sort(reverse=False) # Sort Ascending
print(y)
y.sort(reverse=True) # Sort DeAscending
print(y)

y=["A","C","B","F","D"]
y.sort() # By Default Sort Ascending
print(y)
y.sort(reverse=False) # Sort Ascending
print(y)
y.sort(reverse=True) # Sort DeAscending
print(y)

y=["a","c","b","z","f"]
y.sort() # By Default Sort Ascending
print(y)
y.sort(reverse=False) # Sort Ascending
print(y)
y.sort(reverse=True) # Sort DeAscending
print(y)
print("="*100)
#reverse()-->> Reverse The List Only
z=[1.5,223,"Ahmed",1093,'a']
z.reverse()
print(z)


