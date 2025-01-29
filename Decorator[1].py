def Decorator(func):
    def nestedFunction():
        print("Hello, I Will Decorate Your Function")
        func()
        print("Finished Decoration")
    return  nestedFunction


@Decorator
def Say_Hello():
    print("Hello from Original Function")

Say_Hello()