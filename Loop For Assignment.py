# Assignment 1

My_List=[15, 81, 5, 17, 20, 21, 13]

for i in range(len(My_List)):
    count=0
    if(My_List[i]%5==0):
        print(f"{count} => {My_List[i]}")

print("All Numbers Printed")

# Assignment 2

for i in range(1,21):
    if(i<10):
        if(i==8 or i==6 or i==12):
            continue
        else:
            print("0"+f"{i}")
    else:
        print(i)

print("All Numbers Printed")


