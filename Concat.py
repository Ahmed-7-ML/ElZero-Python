#Concatenation between Strings not Numbers

A="I Love"
B="Python"
print(A+"\n"+B)
print(A+"\t"+B) # or print(A+" "+B)

C=A+" "+B
print(C)

D="My\
 hope\
 to\
 be a\
 good man"

E="I\
 also\
 hope to\
 be a\
 AI Engineer"

print(D+","+E)

# No concatenation with a number
#print("Hello"+10) can only concatenate str (not "int") to str

#Strings
#the text alue may be in single or double quotes
MyStringone='This is Single Quote'
MyStringtwo="This is double Quotes"

print(MyStringone)
print(MyStringtwo)

#you can put " " in '  ' and vice-versa
MyStringthree='U Can Print Double Quotes inside Single Quote"Test"'
MyStringfour="U Can Print single Quote inside Double Quotes'Test'"

print(MyStringthree)
print(MyStringfour)
#Usage of Trible Double Quotes""" """ or Trible Single Quote''' '''
#and we can print single or double quotes in them
MyStringfive="""I Learn
Strings \
Lesson \\\With Osama "Test" 'Test'
ElZero
"""
# Observe The Difference between \ in one end and inside text
MyStringsix="""I Learn
Strings                         
Lesson With\\\ Osama "Test" 'Test'\
ElZero
"""
print(MyStringfive)
print(MyStringsix)