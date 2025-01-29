#	A function is a block of code which only runs when it is called.
#	You can pass data, known as parameters, into a function.
#	A function can return data as a result.

# Function Created To Prevent DRY(Don't Repeat YourSelf)
# Types Of Function: Built-in and User-Defined

# def = Function keyword [Define]

# Examples From My Brain

#01-Function For Welcome:

def Say_Hello(Name):
    print(f"Hello {Name} To Our WebSite \"3A\"!")

# Say_Hello("Ahmed")
# Ebn Akram
#02- Function For Selecting a Task:

def Select_From(Num):
    if Num==1:
        print("Write Function Sin(X,Y).")
    elif Num==2:
        print("Write Function Cos(X,Y).")

def add(n1,n2):
    if type(n1)!=int or type(n2)!= int :
        print("Integer Information Only Allowed")
    else:
        print(n1+n2)


# add(3,"ss")
# add(100,500)

def Full_Name(First,Middle,Last):
    print(f"The Full Name is {First.strip().capitalize()} {Middle.upper():.1s} {Last.strip().capitalize()}")

Full_Name("    ahmed        ","akram", "      amer          ")

MyList=[1,2,3,4,5,6,7,8,9]
print(MyList)
print(*MyList) # UnPack تفريغ

# Function Packing and UnPacking  التعبئة و التفريغ
# Aribitrary Argument:

def say_hello(*people): # People Like a "Tuple" and You Can Access Them
    # for name in people:
    #     print(f"Hello {name.strip().capitalize()}")
    print(type(people))
    print(f"Hello {people[2]}")

say_hello("Ahmed","Akram","Kamel","Amer")


def Show_Details(name,*skills): # Skill is like a Tuple
    print(type(skills))
    print(f"Hello {name} , Your Skills are : ")
    for skill in skills:
        print(f" => {skill}")

MySkill=["C++","Python","SQL"] # Important
Show_Details(*MySkill)

def Family(*names):
    print("Hello Family : ")
    for name in names:
        print(f"  Hello {name}")

Family("Ahmed","Ali")

# Default Parameters:

# Example 1 :
def Say_Hello(name,age,country):
    print(f"Your Name is {name} , Your Age is {age} and Your Country is {country}")

Say_Hello("Ahmed",20,"Egypt")

# Example 2 :
def Say_Hello(name,age,country="UnKnown"):
    print(f"Your Name is {name} , Your Age is {age} and Your Country is {country}")

Say_Hello("Ahmed",20)

# Example 3 :
def Say_Hello(name,age="Unkonwn",country="Unknown"):
    print(f"Your Name is {name} , Your Age is {age} and Your Country is {country}")

Say_Hello("Ahmed")

# Example 1 :
def Say_Hello(name="Unknown",age="Unknown",country="Unknown"):
    print(f"Your Name is {name} , Your Age is {age} and Your Country is {country}")

Say_Hello()


# Aribitrary Keyword Argument **KWARGS Packing and UnPacking
dict1={"HTML":"60%","C++":"90%"}

def Show_Skills(**Skill):
    print(type(Skill)) # Dictionary

    for key,value in Skill.items():
        print(f"{key} => {value}")

Show_Skills(**{"Html":"80%","CSS":"50%" })
Show_Skills(**dict1)
Show_Skills(Html="90%",Cpp='100%')





