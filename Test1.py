# Reading Text Files
# Reading text files involves extracting and processing the data stored within them. 
# 1- Plain Text Files:
#       Plain text files contain unformatted text without any specific structure.
#       You can read plain text files line by line or load the entire content into memory.


# Python's open function is used to create a file object 
# and access the data within a text file. 
# It takes two primary parameters:

# File Path: The file path consists of the filename and directory where the file is located.

# Mode: The mode parameter specifies the purpose of opening the file,
#  such as 'r' for reading, 'x' for creating 'w' for writing, or 'a' for appending.
import os
# print(os.getcwd())
file = open('C:\Users\mr\OneDrive - FEE-MU\Desktop\Files On VSCode\Python\My Text.txt','r')

content = file.read()
# Here, the read() method is called on the file object,
# which reads the entire content of the file and stores it in the variable content.
#  This step effectively loads the entire content of 'file.txt' into memory.

