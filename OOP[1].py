
class Resturant :
    # Constructor
    def __init__(self, n, c_type):
        self.name = n
        self.cuisine_type = c_type
    #Instance Method
    def describe_Res(self):
        print(f"Resturant Name {self.name} & its Cuisine Type {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"Resturant {self.name} is Open")


r1 = Resturant("AboZahra", "Chinese")
r2 = Resturant("Flafal", "French")

r1.describe_Res()
r1.open_restaurant()

r2.describe_Res()
r2.open_restaurant()

# Separator
print("="*50)

class User:
    def __init__(self, f_name, l_name, id, age, gender):
        self.first_name = f_name
        self.last_name = l_name
        self.ID = id
        self.age = age
        self.gender = gender.lower()
    
    def greet_user(self):
        if self.gender == "male":
            print(f"Hello Mr {self.first_name} {self.last_name}")
        elif self.gender == "female":
            print(f"Hello Miss {self.first_name} {self.last_name}")
    
    def describe_user(self):
        print(F"User {self.ID} his Name is {self.first_name} {self.last_name} & his Age {self.age}")

u1 = User("Ahmed", "Akram", "12132", 20, "MALE")
u2 = User("Ibrahim", "Mohamed", "14532", 22 , "MaLE")
u3 = User("Ibrahim", "Mohamed", "14532", 22,"male")
u4 = User("Mona", "Mohamed", "19732", 28,"FemAle")
u5 = User("Salma", "Omar", "17682", 25,"FEMale")



u1.greet_user()
u1.describe_user()

print("-"*50)

u2.greet_user()
u2.describe_user()

print("-"*50)

u3.greet_user()
u3.describe_user()

print("-"*50)

u4.greet_user()
u4.describe_user()

print("-"*50)

u5.greet_user()
u5.describe_user()




