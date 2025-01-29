#------------------------------
#--Dictionary--
#--------------
# [1] Syntax => Dict_Name={Key1:Value1,Key2:Value2,.......}
# [2] Dict Contain Key and Value
# [3] Key Must Be Immutable Such As (Integer,Float,String,Tuple) , List and Dict Not Allowed
# [4] Value May Be Of Any DataType (Integer,Float,String,Tuple,List,Set,Dict)
# [5] Key Must Be Unique (Not Duplicate)
# [6] Dict is UnOrdered(UnIndexed) , U Can Access Element By Key
#------------------------------

user={
    "Name":"Amr",
    "Age" : 20,
    "Country":"Egypt",
    "Skills":["C++","OOP","Data Structure","Algorithms","Python"],
    "Ratings": 10.55,
    "Name":"Ahmed" # Update To Name : Amr ===>> Ahmed
}

# To Print The Dictionary
print(user)
print(type(user))

# To Show Keys
print(user.keys())

# To Show Values
print(user.values())

# To Access Element By Key
print(user['Name'])
print(user['Age'])
print(user['Skills'])

print("="*40)

# Anthor Way By Get Function

print(user.get('Name'))
print(user.get('Age'))
print(user.get('Skills'))

print("="*40)

# Two-Dimensional Dictionary (Nested Dictionary)

Langues={
    'One':{
        'Name':"C++",
        'Progress':"70%"
    },
    'Two':{
        'Name':"Python",
        'Progress':"50%"
    },
    'Three':{
        'Name':"Html",
        'Progress':"60%"
    }
}

print(Langues)

print("="*40)

print(Langues['One'])
print(Langues['Two'])
print(Langues['Three'])

print("="*40)

print(Langues['One']['Name'])
print(Langues['Two']['Name'])
print(Langues['Three']['Name'])

print("="*40)

print(Langues['One']['Progress'])
print(Langues['Two']['Progress'])
print(Langues['Three']['Progress'])

print("="*40)

# Dictionary Length

print(len(Langues))
print(len(Langues['One']))
print(len(Langues['Two']))
print(len(Langues['Three']))

# Create Dictionary From Variables

Father={
    'Name':"Akram",
    'Age':49
}

Mother={
    'Name':"Shimaa",
    'Age':40
}

Brother={
    'Name':"Zeyad",
    'Age':11
}

Sister={
    'Name':"Aya",
    'Age':17
}

Me={
    'Name':"Ahmed",
    'Age':20
}

Family={"One":Me,"Two":Brother,"Three":Sister,"Four":Mother,"Five":Father}

print(Family)

print("="*40)

print(Family['One'])
print(Family['Two'])
print(Family['Three'])
print(Family['Four'])
print(Family['Five'])

print("="*40)

print(Family['One']['Name'])
print(Family['Five']['Age'])
print(Family['Four']['Age'])
print(Family['Three']['Name'])
print(Family['Two']['Name'])

print("="*40)

Test_Dict={"Key1":1,"Key2":"2",(0,1):3.55,2:"Two",3.5:[4,4,5,5,5,6]}

# del(Dict_Name[Key]) =>> To Delete The Item (Key:Value) From Dictionary
# del(Test_Dict['Key1'])
# print(Test_Dict)

if "Key1"  in Test_Dict:
    del(Test_Dict['Key1'])
    print(Test_Dict)
else:
    Test_Dict['Value']=(1,2,5,3,77,8)
    print(Test_Dict)

# 'in' ==>> KeyWord That Check That is The Key In Dictionary Or Not
print("Key2" in Test_Dict) # True / False
print("Value" in Test_Dict) # True / False



