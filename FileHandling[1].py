import os

print(os.getcwd())

# Absloute Path
# file = open(r"C:\Users\mr\OneDrive - FEE-MU\Desktop\Files On VSCode\Python\File Handling\Ahmed.txt", "r")
# print(type(file)) < class '_io.TextIOWrapper' >

# Relative Path
file = open("Ahmed.txt","r")

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
# file = open(r"C:\Users\mr\OneDrive - FEE-MU\Desktop\Files On VSCode\Python\File Handling")

file.close()