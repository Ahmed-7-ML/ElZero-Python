
from time import time

def Speed_Test(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Function Takes {end - start} in Running Time")
    return wrapper

@Speed_Test
def Big_Loop():
    for i in range(1, 100):
        print(i)

Big_Loop()