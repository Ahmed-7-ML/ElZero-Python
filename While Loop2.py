#----------------------
#----PassWord Guess----
#----------------------

Main_Password="AhmedInVsCode"

Tries=5

Input_Password=input("Enter Ypur Password: ")

while Input_Password !=Main_Password and Tries!=0:
    Tries-=1
    # Ternary Operatoe IF
    print(f"Wrong Password.\nAttention: {'Last' if Tries==0 else Tries} Chances Left")
    Input_Password=input("Enter Ypur Password: ")

    if Tries==0 and Input_Password !=Main_Password:
        print("Wrong Password!")
        print("Sorry! , Try again Later.")
        break
else:
    # Main_Password=Input_Password
    print("Congratulations! Password Is Correct!")


