#------------------------------
#--DictMethod1--
# --------------
# [1] clear() => Remove The Elements From Dictionary
# [2] update() => Add New Elements To Dictionary
# [3] copy() => Copy The Elements From Dictionary Into Anthor Dict As A ""Shallow Copy""
# [4] setdefault() => تم شرحها بالامثلة
# [5] items() => Like A Deep Copy
# [6] popitem() => Remove and Return Last Element (Key:Value)
# [7] pop(Key) =>Remove The Key Entered and Return The Corresponding Value
# [8] fromkeys() => Build a Dictionary From External Keys and Values
#------------------------------

Data ={
    "Name":"Ahmed"
}

# clear()
print(Data)
Data.clear()
print(Data)

print("="*40)

Data ={
    "Name":"Ahmed"
}

#Add and Edit
Data['Age']=20
print(Data)

Data["Name"]="Yousef"
Data['Age']=22

print(Data)

print("="*40)

# update()

Data.update({"Country":"Egypt","GPA":3.6})
print(Data)

print("="*40)


# copy() => Shallow Copy

main={"Name":"Ahmed"}
CopyFromMain=main.copy()

print(main)
print(CopyFromMain)

print("="*40)

main['Age']=20

print(main)
print(CopyFromMain) # Shallow Copy Only

print("="*40)

# items() => Like a Deep Copy

c={"One":1,"Two":2}

d=c.items()

print(c)
print(d)

c['One']=4

print(c)
print(d)

print("="*40)

# setdefault()

a={
    "Name":"Ahmed"
}

print(a)
a.setdefault("Name","Osama")
print(a)

a.setdefault("Age",20)
print(a)

a.setdefault("Country")
print(a) # {'Name': 'Ahmed', 'Age': 20, 'Country': None}

print("="*40)


# popitem() =>

a={"one":1,"two":2}

print(a.popitem())
print(a)

a.update({"Age":20}) # a["Age"]=20
print(a)

print(a.popitem())
print(a)

print("="*40)

# pop(Key) => Remove The Key and Return The Value Corresponding To It. 
# If The Key Not Found => Return KeyError

b={
    "Name":"Ahmed",
    "Age":20
}
print(b.pop("Age")) # remove specified key and return the corresponding value

print("="*40)

#fromkeys()

key1="Name"
value1="Ahmed"

key2="Age"
value2=20

print(dict.fromkeys(key1,value1))
print(dict.fromkeys(key2,value2))

print("="*40)