import string
import word from choose_words
import word from IMAGES
def get_available_letters(letters_guessed):
    import string
    letters_left=string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i," ")
    return letters_left

def get_hint(secrete_word,letters_guessed):
    import random
    letters_not_guessed[]
    i=0
    guessed_word=" "
    while (i<len(secrete_word)):
        if secrete_word[i] in letters_guessed:
            guessed_word+=secrete_word[i]
        else:
            guessed_word += "_"
        i=i+1
    return guessed_word

def hangman(secrete_word):
    print("welcome to the game, hangman!")
     print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    letters_guessed = []
    while (True):
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters

        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print "" 
            secrete_word=choose_word()
            hangman(secrete_word)

