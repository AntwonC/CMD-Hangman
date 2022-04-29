import hangman
import random 

global exitVar 

exitVar = True
# Wait for user input
while (exitVar):

    userInputStart = input("Enter S to start the game: ")
    # Only input to start the game
    if userInputStart == 'S':
        randomNumber = random.randint(0, len(hangman.Hangman.wordBank)-1)

        hangmanObj = hangman.Hangman(randomNumber)
        alpha_arr = hangman.create_alphabet_arr()
      

        randomWord = hangmanObj.wordBank[randomNumber]

        
        wordLength = len(randomWord)
        startGame = True

        wordArr = hangman.create_word_arr(randomWord, wordLength)
        blanks = hangman.show_letters(wordLength)
     
        
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
            
            if userGuess == 'W': # Letters available to use
                print(alpha_arr)
            elif userGuess == 'X': # Exit program fully
                startGame = False
                exitVar = False
            elif userGuess == 'C': # Check to see if the letters you guessed are correct
               currentGuessed = hangman.check_Arr(wordArr, blanks, "1")
               print("".join(currentGuessed))
            elif userGuess == 'I': # To enter a guess for the word
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

                    modifiedBlanks = hangman.check_Arr(wordArr, blanks, userGuess)
                    alpha_arr.remove(userGuess)
              
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
