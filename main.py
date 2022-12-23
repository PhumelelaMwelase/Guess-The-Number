import random
import os

# from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    high_responses = ["While admirable, generosity isn't always warranted!", "Much too generous, much too generous!",
                      "A bit overboard, I'd say."]

    low_responses = ["This is no time to be coy, go higher!", "Stinginess is not an attractive characteristic.",
                     "Another stingy one."]
    if guess > answer:
        print(random.choice(high_responses))
        return turns - 1
    elif guess < answer:
        print(random.choice(low_responses))
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    guessed_numbers = []
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            another = input("Would you like to play again? (y/n): ")
            if another == 'y':
                cls()
                game()
            else:
                cls()
                print("Thanks for playing.")
                turns == 0
                return

        elif guess != answer:
            if guess not in guessed_numbers:
                print("Guess again.")
                guessed_numbers.append(guess)
            elif guess in guessed_numbers:
                if len(guessed_numbers) >= 1:
                    print(f"You've already tried number {guess}")
                    print("Guess again.")
                    turns += 1
                    continue

    another = input("Would you like to play again? (y/n): ")
    if another == 'y':
        cls()
        game()
    else:
        cls()
        print("Thanks for playing.")


game()