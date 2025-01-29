#--------------
#--For...Else--
#--------------


My_Numbers=['12','13','14','2','3','5','4','6']

for number in My_Numbers:
    if int(number)%2==0:
        print(f"The number: {number} is Even!")
    else:
        print(f"The number: {number} is Odd!")
else:
    print("Loop Is Finished!")

My_Name="Ahmed Amer"

for letter in My_Name:
    if letter != ' ':
        print(f"This Letter {letter} in my name")



for x in range(20):
    print(x)

print("="*40)

for x in range(14,20):
    print(x)

print("="*40)

for x in range(1,20,3):
    print(x)

print("="*40)