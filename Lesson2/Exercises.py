from random import randint
age = randint(0, 117)

#                                                                              #
# ---------------------- Introduction to Lists ------------------------------- #
#                                                                              #

print("\n------------- Question 01 - 02 ---------------------------------\n")
# 1. Create a list containing the names of five of your close friends.
# Make sure all names are lowercase



# 2. Print the list you've created



print("\n------------- Question 03 --------------------------------------\n")
# 3. How many friends are in this list? Print your answer without manually
# counting the number of names in your list.



print("\n------------- Question 04 --------------------------------------\n")
# 4. Print the first name in your list



print("\n------------- Question 05 --------------------------------------\n")
# 5. Print the last name in your list



print("\n------------- Question 06 --------------------------------------\n")
# 6. Add another friend to the end of your list and print the list



print("\n------------- Question 07 --------------------------------------\n")
# 7. Delete the last person in your list (yeah the one you just added... sorry.)
# Print the list



print("\n------------- Question 08 --------------------------------------\n")
# 8. In two lines of code, remove your best friend from the list and store their
# name in a variable. Print the list after



print("\n------------- Question 09 --------------------------------------\n")
# 9. Put your best friend back into the list where you just pulled them from.
# Print the list



print("\n------------- Question 10 --------------------------------------\n")
# 10. In one line of code, print the last person in your list and remove them
# from the list. Print the list.



print("\n------------- Question 11 --------------------------------------\n")
#                                                                              #
# ---------------------- Organizing Lists ------------------------------------ #
#                                                                              #

# 11. Print your list in alphabetical order without altering the layout of the
# list. Print the list to confirm it hasn't been altered.



print("\n------------- Question 12 --------------------------------------\n")
# 12. Print your list in reverse alphabetical order with out altering the layout
# of the list. Print the list to confirm it hasn't been altered.



print("\n------------- Question 13 --------------------------------------\n")
# 13. Permanently sort your list in alphabetical order and print the list.



print("\n------------- Question 14 --------------------------------------\n")
#                                                                              #
# ---------------------- Looping --------------------------------------------- #
#                                                                              #

# 14. Using a for loop, print all the names in your list



print("\n------------- Questions 15 - 17 ---------------------------------\n")
# 15. Use a for loop to create a list (called 'million_by_for') containing every
# number from 1 to 1,000,000



# 16. Use the list function to create a list (called million_by_list) containing
# every number from 1 to 1,000,000



# 17. In one line of code, create a list of the squares of all odd numbers from
# 1 to 100. Print the list.



#                                                                              #
# ---------------------- if Statements --------------------------------------- #
#                                                                              #

million_sum = 500000500000
second_half_sum = 3750075000

print("\n------------- Question 18 --------------------------------------\n")
# 18. How do we know that we made our million list correctly? We can't exactly
# print all the elements and confirm visually. Use an if statement to confirm
# both that there are one million elements in the list and that sum of all
# elements in the list is equal to the variable 'million_sum'. Confirm both
# lists with a print statement.



print("\n------------- Question 19 --------------------------------------\n")
# 19. If you've confirmed that your lists are correct, confirm that
# second_half_sum is correct. If it's not, correct the variable with the
# right value. The middle starts at 500,000



# These lines are to check if the value you found is correct. Uncomment these
# lines when relevant

#if second_half_sum != 375000750000:
#    print("Sorry, try again")
#else:
#    print("Good job, you may move on")

print("\n------------- Question 20 --------------------------------------\n")
# 20. At the beginning of this file an integer between 0 and 117 and was stored
# in the variable 'age'. Determine the admission price for this imaginary person
# attending an imaginary fair. Print the age of the person and the price of
# admission. Use only one print statement
#
# Ages 0 to 6: FREE
# Ages 7 to 12: $2.50
# Ages 13 to 18: $5
# Ages 19 to 64: $8
# Ages 65+: FREE
