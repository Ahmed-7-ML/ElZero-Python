

file  = open('Ahmed.txt', 'r')

# read, readline, readlines

print(file) # Print Data aout File not Content
print(type(file))
print(file.name)
print(file.mode)
print(file.encoding)

# read
print(file.read()) # Print the Content of file
# print(file.read(10))  # Print First 10 Characters of the content of file

# readline
# print(file.readline()) # read first line
# print(file.readline())  # read second line
# print(file.readline()) # read third line
# and so on

# print(file.readline(10)) # read first 10 charactrs from first line
# print(file.readline()) # read the rest of first line
# print(file.readline()) # read next line line

# readlines
# print(file.readlines()) # print the conetnt of file into list of strings
# print(type(file.readlines()))

# print(file.readlines(10))

# for line in file:
#     if line.startswith("PLA"):
#         break
#     print(line)

# Best Practice => Closing the File

file.close()









