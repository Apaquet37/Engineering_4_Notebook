#Hangman
#Written by Abby Paquette and Elisabeth Scharf

from time import sleep
import os
wrong = 0
  
#Player 1 word request 
word = input("Player 1, type in the secret word: ") #Asking the first person to type in their word, and storing that input
length = len(word) #Getting the length of the secret word
secret = list(word) #Making a list called secret that contains the word
sleep(2) #Waiting for a bit before clearing the screen
os.system('clear') #Clearing the screen (and the secret word) away
spaces = ['_'] * length #A new list called spaces is underscores for each character in the secret word, these are the blanks for the guesser to look at

#Printing the MSP (Man Shaped Piñata)
def msp (x): #Defining the msp function, it is sent the number of wrong guesses that have been made
  #msp = [" 0 ","\\|/ "," |","/ \\ "] -- This is just a helpful line to remind what all the parts of the msp are
  msp = [" 0 "] #The first wrong guess prints the head
  if x >= 2: #If there are two or more wrong guesses
    msp.append(" |") #Add the first section of body
  if x >= 3: #If there are three or more wrong guesses
    msp.append(" |") #Add the second section of body
  if x >= 4: #If there are four or more wrong guesses
    msp.append("/") #Add the first leg
  if x >= 5: #If there are five or more wrong guesses
    msp.pop() #Remove the last element added (the first leg)
    msp.append("/ \\") #And add in both the legs (which to the guesser just looks like the second leg being added)
  if x >= 6: #If there are six or more wrong guesses
    msp.pop(1) #Remove the element in position one (a piece of body)
    msp.insert(1, "\\|") #And replace it with the body plus an arm
  if x == 7: #If there are seven wrong guesses
    msp.pop(1) #Remove the element in position one (the piece of body and the first arm)
    msp.insert(1, "\\|/") #And replace with the full torso
  print(*msp, sep="\n") #Print the MSP as it currently stands

while "_" in spaces and wrong < 7: #While there are still blanks to be guessed and no more than seven incorrect guesses
  print(spaces) #Print the (possibly partially filled in) list of spaces for the guesser to see
  cue2 = input("Player 2, please guess a letter: ") #Ask the guesser for a letter and store that guess
 
  try: #This is a try so it doesn't throw errors if the letter isn't there
    pos = [i for i in range(len(secret)) if secret[i] == cue2] #This looks to see if the letter can be found more than once in the word and returns
                                                               #a list of the positions the letter is found if so
    point = 0 #Point is the number of times the program has run through the while loop that deals with multiple occurrences of the same letter
    val4 = len(pos)  #val4 is a variable that tells us how many times a letter repeats in the word
    while val4 > 1 and val4 != point: #If there is more that one instance of the guessed letter in the word, and we haven't been through this loop
                                      #more than the number of instances
      spaces[pos[point]] = cue2 #This replaces the blank that is in the spot of the array that shows the position of the multiple instances of the
                                #guessed letter with the guessed letter (cue2)
      point = point + 1 #This adds one to the variable point, which shows how many times the while loop has run
    spaces[pos[0]] = cue2 #Replaces the first place a letter occurs in spaces with the letter. This is redundant if the while loop has already
                          #been run through, but it is a good solution for when there is just a single occurrence of a letter

  except: #When the guessed letter isn't part of the word
    print("You are incorrect") #Let the user know they are wrong
    wrong = wrong+1 #Add one to the variable that counts the number of wrong guesses
    msp(wrong) #Call the MSP function and send the number of wrong guesses to it
    
else: #When there are no more blanks or there have been too many incorrect guesses
 print(spaces) #Print how far the user got in the puzzle
 if wrong < 7: #If they had few enough wrong guesses
   print("Congratulations!") #Print congrats
 print("Game over") #Either way print game over
 print("The correct word was: " + word) #Print the correct answer
