import random
import os

def get_guess_results(guess):
    guess_result = ""
    for i in range(len(guess)):
        if guess[i] == word_of_the_day[i]:
            guess_result += "O"
        elif word_of_the_day.find(guess[i]) != -1:
            guess_result += "_"
        else:
            guess_result += "X"
    return guess_result

answer_list = []
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "wordle-answers-alphabetical.txt") 
answer_file = open(file_path, "r")

try:
    with open(file_path, "r") as answer_file:
        answer_list = [x.strip() for x in answer_file]
except FileNotFoundError:
    print("Error: wordle-answers-alphabetical.txt not found.")
    exit(1)

max_num_guesses = 6
current_num_guesses = 1
word_of_the_day = random.choice(answer_list)

print("Welcome to wordle!")
print("You have six guesses to find the word of the day.")
print("After you submit each guess, it will tell you how close you are to the correct word.")
print("X\tThe letter is not in the word.")
print("_\tThe letter is in the word, but in the wrong place.")
print("O\tThe letter is in the correct place!")

while current_num_guesses <= max_num_guesses:
    guess = input("Guess:")

    if guess.lower() == 'exit':
        print("Goodbye!")
        exit()

    while len(guess) != 5:
        print("Your guess must be exactly 5 letters long.")
        guess = input("Guess:")
    
    if not guess.isalpha():
        print("Your guess must only contain letters.")
        continue

    guess = guess.lower()

    if guess == word_of_the_day:
        break

    wordle_results = get_guess_results(guess)

    print("{}\t{}".format(guess, wordle_results))

    current_num_guesses += 1

if current_num_guesses > max_num_guesses:
    print("Better luck next time!")
    print("The word was: {}".format(word_of_the_day))
else:
    print("The word was: {}".format(word_of_the_day))
    print("You won in {} guesses!".format(current_num_guesses))