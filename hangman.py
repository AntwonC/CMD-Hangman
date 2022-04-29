class Hangman:

    wordBank = ["unaccountable", "rightful", "derive", "act", "icicle", "resell", "bird", "frequent","level","questionable","mist","permissible","death","select","geese"]
    
    def __init__(self, number): 
        self.number = number

def check_guesses(guesses, maxGuesses):
    if ( guesses == maxGuesses ):
        return True
    else:
        return False

def show_letters(wordLength):
    underScoreWord = "" 

    for i in range(wordLength): 
        underScoreWord += '_'

    
    return list(underScoreWord)

def check_Arr(wordArr, blanks, userGuess): 
    letterIndex = -1

    for letter in wordArr: 
        letterIndex += 1

        if userGuess == letter: 
            blanks[letterIndex] = letter

    return list(blanks)

def create_word_arr(word, wordLength): 
    wordArr = []
    letterIndex = 0

    for letter in word: 
        wordArr.append(letter)
        
    
    return wordArr

def create_alphabet_arr(): 
    alpha_arr = []
    alphaStartAscii = 97
    alphaEndAscii = 123 

    for num in range(alphaStartAscii, alphaEndAscii): 
        alpha_arr.append(chr(num))  

    return alpha_arr

def check_user_guess(word, userGuess): 
    for letter in word: 
        if userGuess == letter: 
            return True
    
    return False

def check_instant_guess(word, instantGuess): 
    return word == instantGuess
