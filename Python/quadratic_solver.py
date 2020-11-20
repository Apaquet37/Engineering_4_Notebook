#Quadratic Solver
#Written by: Elisabeth Scharf and Abigail Paquette

import array as arr

def quadCalc(a,b,c):
  intA = int(a)
  intB = int(b)
  intC = int(c)
  disc = ((intB*intB)-(4*intA*intC))
  Q1 = (-intB / (2*intA))
  if disc < 0:
    return("The function {0}x^2 + {1}x + {2} has no real roots.".format(intA, intB, intC))
  if disc == 0:
    return("The root is: {0}".format(Q1))
  if disc > 0:
    print("Two roots:")
    pos = ((disc**0.5)/(2*intA))
    w = round((Q1 - pos),5)
    x = round((Q1 + pos),5)
    list = arr.array('d', [w, x])
    return(list)


while True:
    print("Enter the coefficients for ax^2 + bx + c = 0")
    a = input("Enter the first coefficient: ")
    b = input("Enter the second coefficient: ")
    c = input("Enter the third coefficient: ")
    print(quadCalc(a,b,c))
