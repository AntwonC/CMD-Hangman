# CMD-Hangman
A simple hangman project in Python using the command line. 
<br> 

How to run:<br> 
Go into the directory where you downloaded the files. 
Use the command "python3 main.py"<br> 
<br> 
![](https://i.imgur.com/3CFICAL.png)<br> 


**Functions*<br> 
<br> 
------------------------------------------------------------------------------------------------------------<br>
**check_guesses(guesses, maxGuesses)**<br> 

**Parameters**<br> 
guesses: the number of guesses a user has<br> 
maxGuesses: the max amount of guesses a user gets<br> 

**Description**<br> 
This function will check if the user has hit the maximum number of guesses. <br>

**Returns**<br> 
True if guesses == maxGuesses
else
False<br>
------------------------------------------------------------------------------------------------------------<br>
**show_letters(wordLength)**<br> 

**Parameters**<br> 
wordLength: the length of the word the user has to guess<br>

**Description**<br> 
This function will just create a string that are blanks to show the length of the word.<br> 

**Returns**<br> 
A list with the length of the word in underscores<br>
------------------------------------------------------------------------------------------------------------<br>
**check_Arr(wordArr, blanks, userGuess)**<br> 

**Parameters**<br> 
wordArr: the word in array format <br>
blanks: the word in array format <br>
userGuess: the letter user gave as input <br>

**Description**<br> 
This function will check if the user's guess is in the current word. If it is, then it will add every instance of the letter in the word and the change will be reflected in blanks.<br>

**Returns**<br> 
A list with the possibly modified blanks<br>
------------------------------------------------------------------------------------------------------------<br>
**create_word_arr(word, wordLength)**<br> 

**Parameters**<br> 
word: current word to guess <br> 
wordLength: length of the word<br>

**Description**<br> 
This function will append each letter of the word to an array. <br>

**Returns**<br> 
An array with the current word <br>
------------------------------------------------------------------------------------------------------------<br>
**create_alphabet_arr()**<br> 

**Parameters**<br> 
None <br> 

**Description**<br> 
This function will create the alphabet bank which are the letters the user can use to guess the word. It fills the array with the letters a-z using the ascii values. Convert it to the letter using the chr(value) function. <br>

**Returns**<br> 
An array with the alphabet in lowercase. <br>
------------------------------------------------------------------------------------------------------------<br>
**check_user_guess(word, userGuess)**<br> 

**Parameters**<br> 
word: the current word to be guessed <br> 
userGuess: the letter the user guessed <br> 

**Description**<br> 
This function will check the users letter guess to the word if there are any instances of the letter. 

**Returns**<br> 
True if userGuess matches the letter in the word <br>
else <br>
False<br>
------------------------------------------------------------------------------------------------------------<br>
**check_instant_guess(word, instantGuess)**<br> 

**Parameters**<br> 
word: the current word to be guessed <br> 
instantGuess: users word guess<br> 

**Description**<br> 
This function will check the users word guess to the current word to see if they guessed correctly.<br> 

**Returns**<br> 
Returns True if guess is correct<br> 
else<br> 
False<br> 
------------------------------------------------------------------------------------------------------------<br>

The way this program works is by taking advantage of infinite loops and then determining if we should break out of it based on the user input. <br> 

The hangman class located in hangman.py, generates a random number which will take the word from the word bank. Every time the user starts the game, we will create a new hangman object which will get a word. After each game, the word will be different. 
