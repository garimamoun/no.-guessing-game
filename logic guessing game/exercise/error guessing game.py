import random

print(" Welcome to the Guessing Game!")
print("You have only 5 attempts to guess the number.")

number = random.randint(1, 10)
attempts = 5

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(" Congratulations! You guessed the correct number!")
        break
    elif guess < number:
        attempts -= 1
        print(" Too low! Attempts left:", attempts)
    else:
        attempts -= 1
        print(" Too high! Attempts left:", attempts)

if attempts == 0:
    print(" Game Over!")
    print(" The correct number was:", number)
