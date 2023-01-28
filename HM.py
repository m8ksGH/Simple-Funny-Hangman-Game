from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format('WELCOME TO HANGMAN GAME!!!')
colored_ascii = colored(ascii_art, 'yellow')
print(colored_ascii)
name = input("Please enter you name: ")
print("Hi! " + name + " please guess the correct letter enjoy!\n")

import random
import time

hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    |
    |
    |===""", """ 
+---+
  | |
  O |
 /| |
    |
    |
    |===""", """
+---+
  | |
  O |
 /|\|
    |
    |
    |===""", """
+---+
  | |
  O |
 /|\|
  | |
    |
    |===""", """
+---+
  | |
  O |
 /|\|
  | | 
 / \| 
    |===""", """
 
 
"""

]
#list of words for the game
words = ["python", "programming", "computer", "science", "artificial", "functions", "loops", "arithmetic"]

#function to start the game
def start_game():
    #randomly select a word from the list
    word = random.choice(words)
    #set the number of guesses allowed
    max_guesses = 5
    #set the timer
    time_limit = 30
    #initialize the number of guesses made
    guesses_made = 0
    #convert the word to a list of letters
    letters = list(word)
    #create a list of underscores the same length as the word
    underscores = ["_"] * len(word)
    print("You have 30 seconds to guess the word.")
    print(" ".join(underscores))

    #start the timer
    start_time = time.time()
    while "_" in underscores and guesses_made < max_guesses:
        guess = input("Guess a letter: ")
        if guess in letters:
            index = letters.index(guess)
            letters[index] = "_"
            underscores[index] = guess
            print(" ".join(underscores))
            
            elapsed_time = time.time() - start_time
            remaining_time = time_limit - elapsed_time
            print(f"Remaining time: {remaining_time:.0f} seconds")
        else:
            guesses_made += 1
            print("Incorrect! You have " + str(max_guesses - guesses_made) + " guesses left.")
            print(hangman1[guesses_made])
            elapsed_time = time.time() - start_time
            remaining_time = time_limit - elapsed_time
            print(f"Remaining time: {remaining_time:.0f} seconds")

    #end the timer
    end_time = time.time()
    time_taken = end_time - start_time

    if "_" not in underscores:
        print("Congratulations! You won! You took ")
        print(f"{time_taken:.0f}" + " seconds.")
        import tkinter as tk
        root = tk.Tk()
        root.title("Hangman Game!")
        root.geometry("600x700")

        photo = tk.PhotoImage(file= "hmW.png")

        label = tk.Label(root, image= photo, width= 600, height= 700,
        bg= "black", fg= "yellow", font=('Arial',30,'bold'))

        label.pack()

        root.mainloop()

    else:
        print("Sorry, you lost. The word was " + word + " You took ")
        print(f"{time_taken:.0f}" + " seconds.")
        import tkinter as tk
        root = tk.Tk()
        root.title("Hangman Game!")
        root.geometry("600x700")

        photo = tk.PhotoImage(file= "hmL.png")

        label = tk.Label(root, image= photo, width= 600, height= 700,
        bg= "black", fg= "yellow", font=('Arial',30,'bold'))

        label.pack()

        root.mainloop()

    play_again = input("Do you want to play again? (y/n) type y for yes type n for no ")
    if play_again == "y":
        start_game()
    else:
        print("Thanks for playing!")

#start the game
start_game()

