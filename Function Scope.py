
# Scope => Local / Global
x = 1 # Global Scope

def one():
    global x
    x=2
    print(f" From Inside Function One 'S Scope {x}")

def two():
    x=3
    print(f" From Inside Function Two 'S Scope {x}")


print(f" From Global Scope {x}")

one()

print(f" From Global Scope {x}") # OverRided

two()