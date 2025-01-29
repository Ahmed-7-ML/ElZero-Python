# BMI : Body Mass Index = Weight / (Height)**2

weight = float(input("Enter your Weight in Kg: "))
height = float(input("Enter your Length in Meters: "))

BMI = weight / (height) ** 2
print(f"Your BMI = {BMI}")
if BMI < 18.5:
    print("You are UnderWeight")
elif BMI < 24.6:
    print("You are in Normal Range")
elif BMI > 25.9:
    print("You are OverWeigth")
else:
    print("You are Obese")
