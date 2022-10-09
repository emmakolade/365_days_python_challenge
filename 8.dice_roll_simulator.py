# dice roll simulator

import random 
import time 

# define the range of the value of a dice 
min = 1
max = 6

# to loop the rolling through user input 
roll_again = "yes" 

# loop
while roll_again == "yes" or roll_again == "y":
    print("rolling the dice...")
    time.sleep(1.2)
    print("the values are: ")
    
    #to generate and print the 1st random number from 1 - 6
    print(random.randint(min, max))
    time.sleep(1)
    # asking the user to roll again 
    roll_again = input("roll the dices again")