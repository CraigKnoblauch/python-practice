from random import randint
from Statistics import *

# ---------------------------------------------------------------------
# ------------- Section 1: Accepting User Input -----------------------
# ---------------------------------------------------------------------

print("------------------------- Question 1 ----------------------------------")
# 1. Write code that will accept a user input and repeat the input back
# to the user. Perform this in two ways:
#
#       A. Store the input in a variable then use print to display
#       it again.
#
#       and
#
#       B. Use the appropriate function inside the print function
#

print("\n------------------------- Question 1a ---------------------------------")



print("\n------------------------- Question 1b ---------------------------------")



print("\n------------------------- Question 2 ----------------------------------")
# 2. Ask the user to input a number that meets the following criteria:
#
#       Is a value between 1 and 9 inclusive
#       If the number is less than 5, the number must be even
#       If the number is greater than or equal to 5, the number must
#           be odd
#
# You will use this prompt again, so make sure to store the prompt in
# a variable.
#
# Store the user input in the variable 'n'



print("\n------------------------- Question 3 ----------------------------------")
# 3. Using the modulo operator, check the parity of 'n' (parity refers
# to an integer being even or odd). For both outcomes, display the
# value of n and whether it's odd or even.



# ---------------------------------------------------------------------
# ------------------ Section 2: While Loops ---------------------------
# ---------------------------------------------------------------------

print("\n------------------------- Question 4 ----------------------------------")
# 4. Print the numbers 1 through 5 with both a for loop and a while
# loop. Create a new line between the lists



print("\n------------------------- Question 5 ----------------------------------")
# 5. Create a program that prints numbers so long as the user wants
# to continue. For example, the program would print 1, then ask the
# user if it can print 2. If the user approves, the program will
# print 2 and ask if it can print 3. If the user does't approve, the
# program will exit.
#
# It's common to ask for a user decision by presenting (y/n)
#
# Hint: Use a flag



print("\n------------------------- Question 6 ----------------------------------")
# 6. Write a for loop that prints values from 1 to 20. Once 13 is
# printed, terminate the loop



print("\n------------------------- Question 7 ----------------------------------")
# 7. Using a while loop and 'continue', print all even numbers
# from 1 to 12 inclusive.



print("\n------------------------- Question 8 ----------------------------------")
# 8. The 'names' list contains 3-letter, and 4-letter names. Create
# a program that extracts each name from the 'names' list, checks
# the length, and sorts the names into a list for 3-letter names,
# and a list for 4-letter names. Why you're done 'names' should
# be an empty list. Print all three lists at the end.
#
# Hint: use a while loop and the pop method



# ---------------------------------------------------------------------
# --------------------- Challenge Questions ---------------------------
# ---------------------------------------------------------------------
#
# |---------------|
# | Is n correct? |
# |---------------|
print("\n----------------------- Is n correct ----------------------------------")
# The following line of of code wil set the value of 'n' to a
# random 2 digit number:

n = randint(10, 99)

# Your job is to show the user that n is incorrect, and prompt them to
# re-enter a number matching the criteria (criteria from #2). This time,
# you should build code that checks the user's input to make sure it's
# valid.
#
# To make sure your code is set up correctly, enter incorrect values
# to see if you get the appropriate message.



# |----------------------------------|
# | Who's you're favorite president? |
# |----------------------------------|
print("\n-------------- Who's your favorite president? -------------------------")
# The 'presidents' list contains all 45 U.S. presidents, listed in
# order (If you wish to see the presidents list, it can be found in
# Statistics.py, lines 1 through 45). Ask a user to enter the name of
# their favorite president. Display to the user the correct format
# to enter a name. For example, if their favorite president is the
# first George Bush, they should enter
#
#   George H. W. Bush
#
# Retrieve the name from the user check if it is a valid president.
# If the user has entered an incorrect name, let them know, and
# prompt them to re-enter a president name. Once the name checks out,
# use the index method (it may take some googling to figure out
# the best way to use index) to tell the user the number of the
# president. For example, if the user entered Abraham Lincoln, your
# program should reply:
#
#   Abraham Lincoln was president number 16
#
# Note: Be careful with Grover Cleveland, he was both the 22nd and the
# 24th president.
#
# Hint: You may want to construct your prompts first


