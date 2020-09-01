import random

#Introduction
print("WELCOME TO NUMBER GUESSING GAME!!!!")
print("\n\n")

#Declaring number and using the random.randint() function to get a random number from 1 to 9.
number = random.randint(1, 9)

#Using chances as an accumulation variable to increase a chance before it exceeds 5.
chances = 0

#Asking the user for the input of the number that they are guessing.
print("Guess a number between 1 and 9:")

while chances < 5:
    a = input()
    guess = int(a)

    if guess == number:
        print("Congratulations, you have successfully guessed the right number :)")
        break

    elif guess < number:
        print("The number that you have guessed is smaller than the actual number.")

    else:
        print("The number that you have guessed is greater than the actual number.")

    chances += 1

if not chances < 5:
    print("You LOSE, you didn't guess the right number :(")
