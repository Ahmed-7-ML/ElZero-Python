# Methods :

#1-Clear()

a={1,2,3} #Set
b=[1,2,3] #List

print(a.clear()) #None
print(b.clear()) #None

# a.clear()
# b.clear()

print(a) #set()
print(b) #[]

print("="*10)

# Union() same as => Concatenation

c={"Ahmed",True,False}
d={10955,11.65,10.5}
e={"Ali","Akram","aa"}

print(c|d)
print(c.union(d))

print(c|e)
print(c.union(e))

print(c|d|e)
print(c.union(d,e))

x={2,"aa",True}
y={2,"aa",True}
z={2,"aa",True}

print(y|z|x) # If The Sets are Duplicated =>Take One Set

print("="*10)

#Copy()
f={6,7,89,0}

g=f.copy() #Shallow Copy 
#Same As g=f (Assignment)  
print(g)

f.add(5)

print(f)
print(g)

# Remove() && Discard()

h={8,9,0,6,5}

h.remove(5)
# h.remove(7)  KeyError: 7
print(h)

#Remove(Key) => Return Error If Key Not Found
#Discard(Key) => DoesNot Return Error If Key Not Found But Continue in interperting

j={10.9,12.6,13.8,5.5}
j.discard(10.9)
j.discard(10)
print(j)

#pop() =>Remove and Return a Random Element

k={223,4,6,66,7,8,9}
print(k.pop())

#Update() same as=>Union()

l={'d','c',6,8}
zlst=[1,2,3,4,"List"]
n={7.9}

l.update(zlst)
l.update(n)

print(l)




