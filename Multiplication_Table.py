

print("Multiplication Table")

for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i} X {j} = {i*j}")
    if i != 12:
        print('_'*50)