# Assignment 1
def calculate(n1,n2,type_operator=''):

    type_operator=type_operator.strip().lower()

    if(type_operator=='add' or type_operator=='a'):
        return n1+n2

    elif(type_operator==''):
        print('Default Add Operation ')
        return n1+n2

    elif(type_operator=='subtract' or type_operator=='s' ):
        return n1-n2

    elif(type_operator=='multiply' or type_operator=='m'):
        return n1*n2

    elif(type_operator=='division' or type_operator=='d'):
        if n2==0:
            print("Cannot Divide By Zero \"RunTime Erroe\" ")
        else:
            return n1/n2

    else:
        print("Invalid, This Operator is not Exist!")


# n1=int(input())
# n2=int(input())
# operator=input()

# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200

# print(calculate(n1,n2,operator))

print("+"*100)

# Assignment 2

def addition(*numbers):
    sum = 0
    for num in numbers:
        if(num==10):
            continue
        elif(num==5):
            sum-=5
        else:
            sum+=num
    return sum

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160

print("+"*100)

# Assignment 3

def Show_Skill(name,*Skills):
        if len(Skills) == 0:
            print("Hello {} , You Don't Have Skills To Show".format(name))
        else:
            print("Hello {} , Your Skills are : ".format(name)) 
            for Skill in Skills:
                print("- %s"%Skill)

# Input
Show_Skill("Osama", "HTML", "CSS", "JS", "Python")

# Output
"Hello Osama Your Skills Is"
"- HTML"
"- CSS"
"- JS"
"- Python"

# Input
Show_Skill("Ahmed")

# Output
"Hello Ahmed You Have No Skills To Show"

print("+"*100)

# Assignment 4

def Say_Hello(name="UnKnown",Age="UnKnown",Country="UnKnown"):
    return(f"Hello {name} , Your Age is {Age} and You Live in {Country}")

# Input
print(Say_Hello("Osama", 38, "Egypt"))

# Output
"Hello Osama Your Age Is 38 And You Live In Egypt"

# Input
print(Say_Hello())

# Output
"Hello Unknown Your Age Is Unknown And You Live In Unknown"




