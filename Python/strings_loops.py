#Strings and Loops
#Written by Abby Paquette and Elisabeth Scharf

txt = input("Type a simple sentence: ") #Prompting the user and accepting input
letters = list(txt) #Making the input into a list called letters

for i in letters: #Just looping through enough times for each character in the sentence
    newStr = i.replace(' ', '-') #Replacing the spaces with dashes
    print(newStr) #Printing the new sentence that is split up
