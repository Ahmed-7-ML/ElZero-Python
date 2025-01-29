#Set Not Ordered(Unindexed - UnSlicing)
#Set => Immutable Data Type
#Set Contain Immutable Data Types Only(Numbers(int-float) , String , Tuple ) 
#Not Contain List and Dictionary
#Set Items are Unique(Refuse Duplicate Data)
#####################################################################################



set1={1,2,3,"Ahmed"}

print(set1)
print(type(set1))
print(len(set1))


# Set Items are Unique(Refuse Duplicate Data)

set2={1,2,3,"Ahmed",1,2,3,"Ahmed",5,7,8}

print(set2) # Doesnot Show Duplicate Data
print(type(set2))
print(len(set2))  # Doesnot Show Duplicate Data



# (Unindexed - UnSlicing)
# print(set1[0]) TypeError: 'set' object is not subscriptable


#Set => Immutable Data Type (We Cannot Edit It.)
# set1[-1]="Zezo"
# print(set1) TypeError: 'set' object does not support item assignment

#Set Contain Immutable Data Types Only(Numbers(int-float) , String , Tuple ) 
# Not Contain List and Dictionary

# set3={1,2,3,[1,2,4,4,5]}
# print(set3) 
# TypeError: unhashable type: 'list'

set3={1,2,3,4,("Ahmed",1,0,1,1,"Akram"),("Ahmed",1,0,1,1,"Akram")}
print(set3) # Doesnot Show Duplicate Data
print(type(set3))

# Doesnot Show Duplicate Data
print(len(set3)) # Count Tuple as a one Element