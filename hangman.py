from random import choice
from hangman_words import word_list
from hangman_art import logo, stages
while True:

    print(logo)
    word = choice(word_list)
    hangman = len(stages)

    present = []
    for i in word:
        present.append("_")
    out = "".join(present)
    print(out)

    guess_fail = 0
    answers = list(word)
    while "_" in present and guess_fail < hangman:
        guess = input("Enter a letter: ")
        outguess = [guess if guess == answer else "_" for answer in answers]
        if guess in answers:
            for i in range(0, len(answers)):
                if present[i] != "_":
                    present[i] = present[i]
                else:
                    if guess == answers[i]:
                        present[i] = guess
                    else:
                        present[i] = "_"
            print(f"Good job! Successfully guess a letter: {
                  guess}, please continue")
            print("".join(present))
        else:
            guess_fail += 1
            print(stages[7-guess_fail])

    if present == answers:
        print(f"Congrats! You guessed the word:{word}!")
    else:
        print("Sorry, you are hanged!")

    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "n":
        print("Thanks for playing!")
        break
