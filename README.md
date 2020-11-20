# Engineering_4_Notebook
Abby Paquette's Engineering 4 Notebook

## Hello Raspberry Pi
This was my first time ever using a raspberry pi, but this was really just a simple intro assignment. The raspberry pi is a computer, and all it needs is a keyboard, mouse, and monitor to be usable. The biggest hurdle was getting the raspberry pi connected to my computer, but I found that oftentimes a little patience goes a long way and if you wait for the light on the raspberry pi to be completely stable, it will usually work well. Once connected to the computer, I just talked to the pi over serial in a terminal like setting. Then, I ran code that printed hello world 10 times.

[Hello World Code](Python/hello_world.py)
 
<img src="Media/piwiring.jpeg" width="200"><img src="Media/hellocode.png" width="250"><img src="Media/hello_world.png" width="400">

## Get Your Pi Online
The goal of this assignment was fairly simple, to get my pi connected to the internet. Aside from making sure all the syntax was correct in the configuration page, the only part I found tricky was pushing changes I had made to github. I didn't have trouble cloning my repository to the raspberry pi, adding or committing changes, but when I went to push those changes (after I had typed in my email and username) I got a message saying that my repository had been corrupted, and I was no longer able to do any git commands. The way I fixed this was by deleting my repo and then re-cloning it back onto the pi from github.

## Hello Python
In this assignment I had to make a dice roller. The goal was that when the user pressed enter, they would recieve a random number between one and six, and when they pressed "x" and then enter, they would exit the program. This proved to be a fairly simple and short assignment, but it took me a while to get used to the programming environment. My biggest problem was figuring out how to take user input from the keyboard, but I was really just overcomplicating the issue. After looking at some example code, I learned that an easy way to do this is to make a variable that equals user input following some sort of command to the user. In my case that looked like: repeat = input("Press enter to roll or x and enter to quit."). Once you have your variable set to a specific value, you can use if statements to check and see if the user put in one of the specific things you were looking for, and run code based on that. Another new command that I learned is that you can put exit() in your code, and when it runs the program will end. Lastly, I learned how to power down the raspberry pi effectively and help lower the risk of your sd card being corrupted. The basic command for this is sudo shutdown (which shuts down after one minute), but you can also put -h and then a time like now.

[Hello Python Code](Python/dice_roller.py)

<img src="Media/diceroller.png" width="500">

## Calculator
In this assignment I had to make a calculator using python. The goal was to make one function that did the math, and then run through that function five separate times, once for each operation (addition, subtraction, multiplication, division). The program also had to ask the user for the two numbers and receive that input, and print the solutions to the calculations.

The biggest thing I learned while making the calculator was the benefit of collaboration. For this program, I made the entire program in replit, a file sharing site, which allowed me to work at the same time as someone else on the code. This made testing and debugging so much faster, and two minds are almost always better than one. Again, the finished code was really pretty simple, but really using functions and getting used to the ideas of arguments and returns. The argument is what is sent to the function when it is called, in this case the numbers that the user inputted. The return is exactly what it sounds like, what the function returns to the place it was called (most often a loop). For the calculator, there were three parts of the argument, the first two were the numbers to do calculations with, and the third was a number from 1-5 that corresponded with what operation was supposed to happen. This is how we could run the same function 5 times and get the five different desired outputs. One other small tidbit I learned was how to round numbers, specifically in the division portion of this assignment. To round, put round in front of the number, and then at the end put a comma and the number of places you want the result to be rounded to.

[Calculator Code](Python/calculator.py)

<img src="Media/pycalc1.png" width="420"> <img src="Media/pycalc2.png" width="400">
