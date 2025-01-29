#Raise an Exception
name = input("Enter your Name: ")
if not type(name) is int:
    raise ValueError ("String only Allowed")
