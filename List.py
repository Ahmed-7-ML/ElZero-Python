#First Question
Friends=["Amaar","Yousef","Ayman","Karoup","Zeyad"]
print(Friends[0]) # Amaar -->>Method One
print(Friends[-5]) # Amaar -->>Method Two

print(Friends[-1]) # Zeyad -->>Method One
print(Friends[4]) # Zeyad -->>Method Two

print("="*100)

#Second Question
#Slicing
print(Friends[0::2]) #print Items in Even Indices
print(Friends[1::2]) #print Items in Odd Indices

print("="*100)

#Third Question
print(Friends[2:5])
print(Friends[3:5])

print("="*100)

#Fourth Question
Friends[3:5]=["Elzero","Elzero"]
print(Friends)

print("="*100)

#Fifth Question
Friends.insert(0,"ZiZo")
Friends.append("Aya")
#Friends.insert(-1,"Aya")
print(Friends)

print("="*100)

#Sixth Question
# Friends.remove("ZiZo")
# Friends.remove("Amaar")
print(Friends.pop(-1))
print(Friends.pop(0))
print(Friends.pop(1))
print(Friends)
# Friends.remove("Aya")
# print(Friends)

print("="*100)

#Seventh Question
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees) 
friends.extend(school)
print(friends)

print("="*100)

#Eighth Question
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort(reverse=False)
print(friends)

friends.sort(reverse=True)
print(friends)

#Number Ten Question
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0]) #Django
print(technologies[4][0]) #Django
print(technologies[4][2]) #Web
print(technologies[4][1]) #Flask

# Needed Output
# Django
# Web
