class Car:
    #C lass attributes are variables that are shared among all instances (objects)
    # of the class.
    # They are defined within the class but outside of any methods.
    max_speed = 120

    def __init__(self, makerOfCar, modelOfCar, colorOfCar, speedOfCar=0): #speed is an optional parameter
        self.color = colorOfCar
        self.make = makerOfCar
        self.model = modelOfCar
        self.speed = speedOfCar

    def accelerate(self, acceleration):
        # that allows the car to accelerate. 
        #If the acceleration does not exceed the max_speed, update the car's speed attribute.
        # Otherwise, set the speed to the max_speed.
        if (self.speed + acceleration <= Car.max_speed):
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    def Get_Speed(self):
        # that returns the current speed of the car.
        return self.speed



#car1: Make = "Toyota", Model = "Camry", Color = "Blue"

car1 = Car("Toyota", "Camry","Blue")
car1.accelerate(20)

# car2: Make = "Honda", Model = "Civic", Color = "Red"
car2 = Car("Honda", "Civic", "Red")
car1.accelerate(30)

print(f"{car1.make} {car1.model} is currently at {car1.Get_Speed()} km/h")
print(f"{car2.make} {car2.model} is currently at {car2.Get_Speed()} km/h.")

# # Find out the methods can be used on the object
print(dir(Car))

