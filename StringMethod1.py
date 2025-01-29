#String Method Lesson 1
# We Have Some Built-in Functions : len(),strip(),rstrip(),lstrip()
# capitalize(),title(),zfill(),lower(),upper()

s="Five"
print(len(s)) #return The Number of Characters of a string o/p=4
print(len("Ahmed Akram")) #o/p=11

print("Ahmed"*2) # Will Repeat "Ahmed" Twice
print("Pyyhon is Pretty "*3) # Will Repeat "Python is Pretty" Third



#1- strip() ,rstrip()& lstrip() -->> Remove Characters but not in middle
s="    Python    "
print(s.strip()) #O/P=Python
print(s.rstrip()) #O/P=    Python 
print(s.lstrip())# O/P=Python

#If We Want To Remove a Special Character
s="PPythonPPppp"
print(s.strip("#"))
print(s.rstrip("#"))
print(s.lstrip("#"))
print(s.strip("P"))

#2-title() & captialize()
s=" 3d animiation by ahmed akram"
print(s.title())
r="ahmed akram is a data analyist"
print(r.capitalize())
print(r.title())

#3- upper() & lower()

r="swimming"
print(r.upper())
r="AHMED"
print(r.lower())
###############________________________________________####################
