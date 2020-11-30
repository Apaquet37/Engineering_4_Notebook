#Strings and Loops
#Written by Abby Paquette and Elisabeth Scharf

import numpy as np

txt = input("Type a simple sentence: ")

letters = list(txt)

array1 = np.array(letters)
k = []

for i in letters:
    newStr = i.replace(' ', '-')
    print(newStr)
