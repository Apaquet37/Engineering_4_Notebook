#Calculator
#Written by: Abigail Paquette and Elisabeth Scharf
num = 1 #This is a variable we made to control how many times certain sections run
def doMath(a,b,c): #This is the function that does all the math for our calculator, it receives a, b, and c from the loop when called
  int1 = int(a) #Making each of the numbers a variable and integer within the function
  int2 = int(b) #a and b are the numbers that the user inputted for calculations
  rep = int(c) #c is a variable that indicates which operation should be performed
  #print(rep)
  if rep == 1: #When the third number sent to doMath is 1
    return("The sum is: " + str(int1 + int2)) #Addition is performed and the sum is returned
  if rep ==2:
    return("The difference is:" + str(int1-int2)) #Subtraction
  if rep == 3:
    return("The product is:" + str(int1*int2)) #Multiplication
  if rep == 4:
    div = round((int1/int2),2) #The division is being performed and rounded here, before being added into the string with text to be returned
    return("The quotient is:" + (str(div)))
  if rep == 5:
    return("The modulo is:" + str(int1%int2)) #Modulo


while True:
  if num == 1: #Using num was our (possibly now unnecessary) system of making sure that the program only asked for inputs once before all the calculations were completed
    a = input("Please enter you first number:") #The user puts in their first number, followed by enter, and that is stored as a
    b = input("Please enter your second number:") #b is the second user inputted number
    num = 2 #Changing num to 2 so it doesn't run back through these prompts
  print(doMath(a,b,1)) #These lines call the function doMath, and send three numbers to it
  print(doMath(a,b,2)) #The first two numbers are the numbers the user put in, and the third number indicates which operation should be performed
  print(doMath(a,b,3)) #What is being returned from the function is printed, and those are the calculations
  print(doMath(a,b,4))
  print(doMath(a,b,5))
  num = 1 #Once all the calculations have been made and printed, the prompt to input numbers comes back up to start the process over
