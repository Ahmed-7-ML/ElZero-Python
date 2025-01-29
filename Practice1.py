# Car dealership's inventory management system #

# Task-1. 
# You are tasked with creating a Python program to
# represent vehicles using a class.
# Each car should have attributes for maximum speed and mileage.
# Task-2.
# Update the class with the default color for all vehicles," white".
# Task-3. 
# Additionally, you need to create methods in the Vehicle class to
# assign seating capacity to a vehicle
# Task-4. 
# Create a method to display all the properties of an object of the class.
# Task-5. 
# Additionally, you need to create two objects of the Vehicle class 
# object that should have a max speed of 200kmph and mileage of 20kmpl with 
# five seating capacities, and 
# another car object should have a max speed of 180kmph and mileage of 25kmpl 
# with four seating capacities.

class vehicles:
    color = "White"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_prop(self):
        print("Properities of a Car:")
        print("Maximum Speed : ", self.max_speed)
        print("Mileage : ", self.mileage)
        print("Color : ", self.color)
        print("Seating Capacity : ", self.seating_capacity)


car1 = vehicles(200, 20)
car1.seating_capacity(5)
car1.display_prop()

car2 = vehicles(180, 25)
car2.seating_capacity(4)
car2.display_prop()
