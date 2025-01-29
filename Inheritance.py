class Person:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def print_name(self):
        print(f"Your Name is {self.first_name} {self.last_name} from Base Class ")

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname) 
        super().__init__(fname, lname)

        self.year = year
    def welcome(self):
        print(f"Welcome Student {self.first_name} {self.last_name} your Graduation Year {self.year}")
    
    # Method with the same name of method in parent class
    
    # def print_name(self): # Not Override
    #     return super().print_name()

    def print_name(self): # Overrie
        print(f"Hello Student {self.first_name} {self.last_name} from Derived Class")
    

p1 = Person("Ahmed", "Akram")
p1.print_name()

s1 = Student("Omar", "Kamal", "2020")
s1.print_name()
s1.welcome()
