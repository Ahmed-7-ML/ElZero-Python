#----------------------------
#--Simple BookMarks Manager--
#----------------------------

# Empty List To Fill Later
My_Favourite_Webs=[]

# Maximum Number Of Websites You Must Add
MaxNumWebs=int(input("Enter The Number Of Webs That You Want To Save In Book Mark : "))

while MaxNumWebs>0:
    Web=input("Add Your Web Without \"https://\"  ")
    My_Favourite_Webs.append(f"https://{Web.strip().lower()}")
    MaxNumWebs-=1
    print(f"Website Added , {MaxNumWebs} Places In BookMark Left")
    print(My_Favourite_Webs)
else:
    print("="*40)
    print('BookMark Is Full , You Can\'t Add More')
    print(f"Full BookMark {My_Favourite_Webs}")

if len(My_Favourite_Webs)>0 : # Not Empty List
    My_Favourite_Webs.sort()

    index=0
    print("The BookMark Details : ")
    print("-"*10)

    while index<len(My_Favourite_Webs):
        print(f"#{index+1} {My_Favourite_Webs[index]}")
        index+=1
else :
    print("The List Is Empty, Sorry!!")

print("-"*10)
