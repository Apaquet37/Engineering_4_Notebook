#Strings and Loops
#Written by Abby Paquette and Elisabeth Scharf

import numpy as np #This is the library for arrays

txt = input("Type a simple sentence: ") #Prompting the user and accepting input
letters = list(txt) #Making the input into a list called letters
array1 = np.array(letters) #Making the list into an array

for i in letters: #Just looping through enough times for each character in the sentence
    newStr = i.replace(' ', '-') #Replacing the spaces with dashes
    print(newStr) #Printing the new sentence that is split up
