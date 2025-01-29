# Difference() same as =>> Set1-Set2

a={1,2,3,4}
b={1,2,"Ahmed","Akram"}

print(a)
# print(a-b)
print(a.difference(b))
print(a)
# (a-b) != (b-a)
print(b)
# print(b-a)
print(b.difference(a))
print(b)

# print(a-a) # Empty Set
print(a.difference(a)) #Empty Set

# print(b-b) # Empty Set
print(b.difference(b)) # Empty Set

print("="*40)

#Difference_Update =>> Find The Difference And Assign The List By This Difference
# same as Set1=Set1-Set2  (Find The Difference and Assign "Update" )

c={1,2,3,4}
d={1,2,4,5}

# print(c.difference_update(d)) Why None????

print(d)
d.difference_update(c)
print(d)

c={1,2,3,4}
d={1,2,4,5}

print(c)
c.difference_update(d)
print(c)

c={1,2,3,4}
d={1,2,4,5}

print(c)
c.difference_update(c)
print(c)

c={1,2,3,4}
d={1,2,4,5}

print(d)
d.difference_update(d)
print(d)

print("="*40)

# Intersection() => ايجاد التقاطع 
# Set1&Set2

e={1,2,3,"X","Y"}
f={5,6,7,1,"X"}

print(e)
# print(e.intersection(f))
print(e&f)
print(e)

print(f)
# print(f.intersection(e))
print(f&e)
print(f)

print("="*40)

#Intersection_Update() => ايجاد التقاطع و يجدد المجموعه لهذه القيمة (التقاطع)
# same as Set1=Set1&Set2

e={1,2,3,"X","Y"}
f={5,6,7,1,"X"}

print(e)
# e.intersection_update(f)
e=e&f
print(e)

print(f)
# f.intersection_update(e)
f=f&e
print(f)

print("="*40)

#Symmetric_Difference() =>> ايجاد عدم التقاطع 
# same as Set1^Set2

Set1={1,2,3,4,"Y"}
Set2={5,6,"Y",2,3,1}

print(Set1)
# print(Set1^Set2)
print(Set1.symmetric_difference(Set2))
print(Set1)

Set1={1,2,3,4,"Y"}
Set2={5,6,"Y",2,3,1}

print(Set2)
print(Set2^Set1)
# print(Set2.symmetric_difference(Set1))
print(Set2)

print("="*40)

#Symmetric_Difference_Update() =>> ايجاد عدم التقاطع وعمل تجديد للمجموعه بهذه القيمة(عدم التقاطع)
# same as ٍSet1=Set1^Set2

Set1={1,2,3,4,"Y"}
Set2={5,6,"Y",2,3,1}

print(Set1)
# Set1=Set1^Set2
Set1=Set1.symmetric_difference(Set2)
print(Set1)

Set1={1,2,3,4,"Y"}
Set2={5,6,"Y",2,3,1}

print(Set2)
# Set2=Set2^Set1
Set2=Set2.symmetric_difference(Set1)
print(Set2)

print("="*40)

#FINISH الحمدلله