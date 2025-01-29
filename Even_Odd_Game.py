# Build a simple Project that takes a number from user and tell the user that is odd or even
# If user Press small case 'x' => Exit the Game
# If user entered any letter rather than 'x' => tell him to enter valid number
# The game continue even after i get the result

# Even => n % 2 == 0
# Odd => n % 2  != 0

print("Welcome to Even/Odd Game!")
print("Enter a number and i will tell you that is even or odd?")
print("Press 'x' if you want to exit the game!")


while True:
    N = input("Enter a Number :").lower()

    if N == 'x':
        print("Closing The Game!")
        print("Thanks...")
        break

    try:
        N = float(N)

        if N % 2 == 0:
            print(f" {N} is Even !")
        else:
            print(f" {N} is Odd !")

    except ValueError:
        print("Please, Enter a Valid Number!")
    print('-'*50)



