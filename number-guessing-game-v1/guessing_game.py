"""
Python Development Tech-degree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

# Create the start_game function.
def start_game():
 guess = 0
tries = 0

    # Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
print("Hello! welcome to the random number guessing game, all you have to do is guess the random number between (1- 10) and you win!")
#   2. Store a random number as the answer/solution.
solution = random.randint(0,11)
while guess != solution:
    guess = int(input)("Enter a guess from (1 - 10)")
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
if guess > solution:
    print("it's lower")
    tries+= 1

#     b. If the guess is less than the solution, display to the player "It's higher".
elif guess < solution:
    print("it's higher")
    tries+=1
else:
    ("you guessed right,you won!")
    



#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
print(f"it took you {tries} tries to get the right answer, the game is ending now bye!")
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to.)


# Kick off the program by calling the start_game function.
start_game()
