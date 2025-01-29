# 1- Continue

my_numbers=[1,2,3,5,7,8,9,10,13]

for num in my_numbers:
    if num==9:
        continue
    print(num)

print("*"*10)

for num in my_numbers: # Continue Here Has No Effect
    print(num)
    if num==9:
        continue

print("*"*10)

# 2- Break
for num in my_numbers: 
    if num==9:
        break
    print(num)

print("*"*10)

for num in my_numbers:
    print(num)
    if num==9:
        break

print("*"*10)

# 3- Pass
#"function definitions" OR "If Statement" OR "For Loop" OR "While Loop" OR 
# Any Thing Have Block OF Code
# cannot be empty, but if you for some reason have a 
# function definitions OR If Statement OR For Loop OR While Loop OR 
# Any Thing Have Block OF Code 
# with no content, put in the ((((("pass"))))) statement 
# to avoid getting an error.
for num in my_numbers:
    if num==9:
        pass
    print(num)

print("*"*10)

for num in my_numbers:
    print(num)
    if num==9:
        pass


