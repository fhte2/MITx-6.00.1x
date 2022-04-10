# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    word = sorted(set(list(secretWord)))
    guessed = sorted(lettersGuessed)
    
    if word == guessed:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    word = [letter if letter in lettersGuessed else '_' for letter in secretWord]

    result = ' '.join(word)

    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    import string

    letters = string.ascii_lowercase

    unguessed = [x for x in letters if x not in lettersGuessed]

    res = ''.join(unguessed)

    return res
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman')
    print(f'I am thinking of a word that is {len(secretWord)} characters long.')

    import string

    letters_guessed = []
    word_progress = ''

    count = 8 

    while count > 0:
      print(f'You have {count} guesses left.')

      available_letters = getAvailableLetters(letters_guessed)

      print(f'Available letters: {available_letters}')

      letter_guessed = str(input('Please guess a letter:'))
      print(' ' + letter_guessed)

      if letter_guessed in secretWord and letter_guessed in available_letters:

        letters_guessed.append(letter_guessed)

        if isWordGuessed(secretWord, letters_guessed):
          print('Congratulations, you won!')
          quit()

        word_progress = getGuessedWord(secretWord, letters_guessed)
        print(f'Good guess: {word_progress}')

      elif letter_guessed in secretWord and letter_guessed not in available_letters:
        print(f"Oops! You've already guessed that letter: {word_progress}")

      elif letter_guessed not in secretWord:
        print(f"Oops! That letter is not in my word: {word_progress}")
      
      else:
        print('what is going ion')  

      count -= 1  

    print(f'Sorry, you ran out of guesses. The word was {secretWord}')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
