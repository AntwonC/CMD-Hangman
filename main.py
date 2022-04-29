import hangman
import random 

global exitVar 

exitVar = True

while (exitVar):

    userInputStart = input("Enter S to start the game: ")

    if userInputStart == 'S':
        randomNumber = random.randint(0, len(hangman.Hangman.wordBank)-1)

        hangmanObj = hangman.Hangman(randomNumber)
        alpha_arr = hangman.create_alphabet_arr()
       # print(alpha_dict)

        randomWord = hangmanObj.wordBank[randomNumber]

        #print("Random Number: ", randomNumber)
        #print("Random Word: ", randomWord)
        
        wordLength = len(randomWord)
        startGame = True

        wordArr = hangman.create_word_arr(randomWord, wordLength)
        blanks = hangman.show_letters(wordLength)
        #print(wordArr)
        
        print("".join(blanks))

        guesses = 0
        maxGuesses = 5
        # Enter game here 
        while (startGame): 
            print("You have", maxGuesses-guesses+1, "guesses left.")
            userGuess = input(
"""
Enter 'W' for remaining letters
Enter 'I' to guess the word
Enter 'X' to quit program
Enter 'C' to see guessed letters
Enter letter to guess
    
Enter letter: """
)
            
            if userGuess == 'W': 
                print(alpha_arr)
            elif userGuess == 'X': 
                startGame = False
                exitVar = False
            elif userGuess == 'C': 
               currentGuessed = hangman.check_Arr(wordArr, blanks, "1")
               print("".join(currentGuessed))
            elif userGuess == 'I': 
                instantGuess = input("Enter your word guess here: ")

                word_guess = hangman.check_instant_guess(randomWord, instantGuess)
                
                if word_guess: 
                    print("You guessed the word!")
                    startGame = False
                else: 
                    guesses += 1
                    print("You used a guess. You have", maxGuesses-guesses+1, "guesses left.\n")

            elif len(userGuess) == 1 and userGuess.isalpha():
                if ( hangman.check_user_guess(randomWord, userGuess)):
                    #wordDict[userGuess] = 1
                    #print(wordDict)
                    modifiedBlanks = hangman.check_Arr(wordArr, blanks, userGuess)
                    alpha_arr.remove(userGuess)
                   # "".join(modifiedBlanks)
                    print("".join(modifiedBlanks))
                else: 
                    if ( hangman.check_guesses(guesses, maxGuesses) ):
                        print("You used all your guesses. Game over!")
                        startGame = False 
                    else:
                        guesses += 1
                        print("You guessed the letter wrong. You have", maxGuesses-guesses+1, "guesses left.\n")
            else:
                print("Please enter one letter")
                #print(hangmanObj.head)
                #print("Gotta code the next steps...") 



    #else: 
        #userInputStart = input("Enter S to start the game: ")
    



#print(hangmanObj.number)