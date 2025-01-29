print("Welcome to Sum Game!")
print("This Game takes anumber and return the Sum and Average!")
print("Press 'X' if you want to Exit the Game!")

count = int(input("How Many Numners you will entered ? : "))

sum = 0
for i in range(count):
    try:
        N =input(f"Enter the {i+1}th Number : ")
        if N == 'x':
            print("Closing The Game")
            print("Thanks..")
            break
        else:
            N = float(N)
            print('-'*10)
            sum += N
    except ValueError:
        print("Enter a valid Number!")

print(f"Sum of Numbers = {sum}")
print(f"Average of Numbers = {sum / count}")
print("Thanks...")




