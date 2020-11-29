#Quadratic Solver
#Written by: Elisabeth Scharf and Abigail Paquette

def quadCalc(a,b,c): #Defining the function, it uses the 3 arguments, a b and c, that were sent to it.
  intA = int(a) #The integer, a, that was inputted by the user in the loop is changed to a variable the function can work with. The x^2 coefficient
  intB = int(b) #The x coefficient
  intC = int(c) #The constant
  disc = ((intB*intB)-(4*intA*intC)) #Finding the discriminant: b squared minus the quantity 4 times a times c
  Q1 = (-intB / (2*intA)) #This is the other part of the quadratic formula that isn't the discriminant: negative b over 2a
  if disc < 0: #If the discriminant is less than zero, there are no real roots, because that would be the square root of a negative
    return("The function {0}x^2 + {1}x + {2} has no real roots.".format(intA, intB, intC)) #Returns a message to be printed
  if disc == 0: #If the discriminant equals zero, there is only one root, Q1, at which there is a multiplicity
    return("The root is: {0}".format(Q1)) #Again returning a message with the root to be printed
  if disc > 0: #If the discriminant is greater than zero, then there will be two real roots
    pos = ((disc**0.5)/(2*intA)) #This is a variable that equals half the discriminant over 2a, or: (1/2((b^2)-4ac))/2a
    w = round((Q1 - pos),5) #The two roots are w and x, and they are rounded to five decimal places
    x = round((Q1 + pos),5) #The math in this is doing the quadratic formula, using variables we have already established. 
                            #The two separate roots are for the plus and minus
    return([w,x]) #This is returning an array with the two roots


while True:
    print("Enter the coefficients for ax^2 + bx + c = 0") #Asking for user input to form a quadratic
    a = input("Enter the first coefficient: ") #Inputting the coefficient for x squared. This is a
    b = input("Enter the second coefficient: ") #Inputting the coefficient for x. This is b
    c = input("Enter the third coefficient: ") #Inputting the constant. This is c
    returnVal = quadCalc(a,b,c) #Calling the function and sending a, b, and c to it. The return is then set to equal a variable called returnVal
    if isinstance(returnVal,list): #If the return value is an array, then print "Two roots:" and then the roots
      print("Two roots:")
      for root in returnVal:
        print(root)
    else:
      print(returnVal) #Otherwise, just print what the function returned
