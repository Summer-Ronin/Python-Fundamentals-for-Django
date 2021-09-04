###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
from rich.console import Console

console = Console()


def computer_gen():
    """
        Computer thinks of 3 digit number
    """
    digits = list(range(1, 10))

    # Shuffle the digits
    random.shuffle(digits)

    # Get first 3 digits from the list
    # return int(''.join([str(i) for i in digits[:3]]))
    return digits[:3]

def make_usr_list(user_input):
    """
        Convert user input string into a list
        Input: a 3 digit number
        Output: a list
    """
    return_list = []
    while user_input != 0:
        return_list.append(user_input % 10)
        user_input = user_input // 10
    
    # We have to reverse the list since we append from 
    return return_list[::-1]

def check_guess(comp_numb, user_guess):
    """
        Compare user guess with computer gen number
        Input: computer gen number, user guess number
        Output: a statement
    """
    if comp_numb == user_guess: 
        return 'BREAK'
    
# User input
console.print("It's a three digit number, what is your guess?", style="cyan2")

# It stands out there because if you put it in while loop, computer will change the number every single
# time the loop loops back
computer_number = computer_gen()

# Comment this line so the game can be fully achieved
print(computer_number)

flag = True
while flag == True:
    user_guess = input()

    user_guess_list = make_usr_list(int(user_guess))

    if((user_guess_list == computer_number) == True):
        console.print('HOORAY, MATCH...', style="cyan")
        flag = False

    elif(user_guess_list[0] in computer_number or user_guess_list[1] in computer_number or user_guess_list[2] in computer_number):
        console.print('Closed! but not enough, guess again', style="red")
        console.print(user_guess_list == computer_number)

    else: 
        console.print('Nope! nothing matches, guess again', style="red")


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
