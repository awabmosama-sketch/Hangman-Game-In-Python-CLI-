import random
from lists import already_guessed,guessedchar,small_alphabets,hangman_words
from pics import HANGMAN_PICS


#---variables---
wrong_guesses = 0
secretword = random.choice(hangman_words)
guessedchar = ["_"] * len(secretword)
#----------------

print("\n\n")
print("Welcome to Hangman! \n\n\n")
print(" ".join(guessedchar))
print("\n")


while wrong_guesses <6 :   
    #---- Input -----
    guessedcharacter = input("Enter Your Guess Character ? :").strip().lower()
    #---- Cleaner ----
    if len(guessedcharacter) != 1 or guessedcharacter not in small_alphabets:
        print("Please Enter A Single Letter From [A-Z] ! \n")
        continue
    #---- Reject Duplicate -----
    if guessedcharacter in already_guessed:
        print(f"You Already Guessed The Letter ,{guessedcharacter}, Try Again \n")
        continue
    #---- Appends The Unguessed Characters ----
    already_guessed.append(guessedcharacter)
    #---- Checks If The Guesses Is In The SecretWord ----
    if guessedcharacter in secretword:
        print(f"The Letter ,{guessedcharacter}, Is In The Word !")
        i=0
        while(i < len(secretword)):
            if secretword[i] == guessedcharacter:
                guessedchar[i] = guessedcharacter
            i += 1
    #---- Else The Tries Will Decrease ----
    else:
        print(f"Sorry ,{guessedcharacter}, Is Not In The Word !")
        wrong_guesses += 1
        print(f"The Remaining Tries : {6 - wrong_guesses}")

    #---- draw the Gallow and the hangman
    if wrong_guesses ==0:
        print(HANGMAN_PICS[0])
    if wrong_guesses ==1:
        print(HANGMAN_PICS[1])
    if wrong_guesses ==2:
        print(HANGMAN_PICS[2])
    if wrong_guesses ==3:
        print(HANGMAN_PICS[3])
    if wrong_guesses ==4:
        print(HANGMAN_PICS[4])
    if wrong_guesses ==5:
        print(HANGMAN_PICS[5])

    #---- Reveals The List ----
    print(" ".join(guessedchar))
    #---- Print The Win Statement ----
    if "_" not in guessedchar:
        print(f"Congratulations! You guessed the word ,{secretword}, and won!")
    #---- Print The Lose Statement ----
    if wrong_guesses == 6:
        print(HANGMAN_PICS[6])
        print(f"Game Over ! \n The Secret Word Is ,{secretword},")