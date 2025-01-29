

def Decorator1 (func):

    def nestedFunc(n1, n2):

        if n2 < 0:
            print("Seconnd Number is Less than Zero\nThe Result may be negative")
        func(n1, n2)
    return  nestedFunc


def Decorator2(func):

    def nestedFunc(n1, n2):
        print("From Decorator2 ")
        func(n1, n2)
    return nestedFunc

# For UnLimited Number of Parameters
def Decorator3(func):
    def nestedFunc(*numbers):
        print("From Decorator Three ")
        func(*numbers)
    return nestedFunc

@Decorator2
@Decorator1
def  Subtract(num1, num2):
    print(f"Subtraction : {num1 - num2} ")

Subtract(10, -2)

print("="*50)

@Decorator3
def Add(n1, n2, n3, n4):
    print(n1+ n2+ n3+ n4)


Add(1,2,3,4)
