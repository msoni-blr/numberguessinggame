import random

start = 1
end = 100
random_number = random.randint(start, end)

while True:
    command = input(f"Guess the number between {start} and {end}: ")
    try:
        input_number = int(command)
        if input_number > random_number:
            print("Too high!")
        elif input_number < random_number:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number")
