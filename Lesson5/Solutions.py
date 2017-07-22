from random import randint

# How this file works:
#
# You will be asked to make a multiple of functions. You may create
# non-function code to test your functions, but this file, up to
# Section 3, must contain ONLY FUNCTIONS.
#
# ---------------------------------------------------------------------
# -------- Section 1: Function Definition and Use of Arguments --------
# ---------------------------------------------------------------------

print("------------------------- Question 1 ----------------------------------")
# 1. Question 1 is split into three parts. Make three separate
# functions corresponding to each part.
#
#       a. Create a function that prints:
#           Question 1a: Printing without an Argument
#
#       Name this function 'question_1a'
#


def question_1a():
    print("Question 1a: Printing without an Argument")

#       b. Create a function that requires an argument. Use the
#       argument in a print statement. For example, if your
#       argument was "sarah", your function would print:
#           Question 1b: Printing with "sarah" as the argument
#
#       Name this function 'question_1b'


def question_1b(arg):
    print("Question 1b: Printing with \"" + arg + "\" as the argument")

#       c. Create a function that combines both functionalities
#       of the previous functions
#
#       Name this function 'question_1c'
#
#       Hint: Use a default value


def question_1c(arg= ''):
    if arg:
        print("Question 1c: Printing with \"" + arg + "\" as the argument")
    else:
        print("Question 1c: Printing without an Argument")

# 2. Create a function (call it question_2) with two string parameters.
# The purpose of this function will be to print information about a pet.
# The two parameters must be the name of the pet and the type of animal.
# The function must print a description of the pet. Default values may
# be given to the parameters, but are not required.


def quesion_2(name, animal):
    print("My " + animal + "\'s name is " + name.title())

# 3. Create a function (call it question_3) that has an arbitrary amount
# of parameters. For each argument given to the function, print the
# argument, as well as which number it is. Start counting from 1


def question_3(*args):
    count = 1
    for a in args:
        print(a + " is #" + str(count))
        count += 1

# ---------------------------------------------------------------------
# -------------------- Section 2: Return Values -----------------------
# ---------------------------------------------------------------------

# 4. Create a function (call it question_4) that will accept a single
# argument and put it into a string. Return that string. For example,
# if the argument given is "peanuts", question_4 will return:
#
#   question_4 is returning "peanuts"


def question_4(arg):
    return "question_4 is returning \"" + arg + "\""

# 5. Create a function (call it question_5) with one parameter. When
# the function is called, a number will be used as argument. The
# function will create and return a list of numbers. The first element
# of this list will be the number provided, and each number after
# will be incremented by 5 until there are 5 numbers in the list.
#
# So, if the function is given 20 as an argument, the resulting list
# will be:
#
#    [20, 25, 30, 35, 40]
#
# Hint: You will need to use a while loop


def question_5(n):
    l = [n]
    while not len(l) == 5:
        n += 5
        l.append(n)

    return l

# 6. Mini-Challenge: Create a function (call it question_6) that
# accepts an arbitrary amount of key-value pairs. This function
# must create and return a dictionary, constructed from these pairs


def question_6(**pairs):
    d = {}
    for k, v in pairs.items():
        d[k] = v

    return d

# ---------------------------------------------------------------------
# -------------------- Section 3: Modules -----------------------------
# ---------------------------------------------------------------------

# Commonly, when you begin a file, you should always put your import
# statements at the top of the page. However, to keep this file
# collected, you will use an import statement at the start of each
# question. This way, we can sort of pretend that each question is its
# own file.
#
# For the following questions, you will need to read the documentation
# on the functions you will be asked to import and use. A question will
# ask you to perhaps import a function and use it appropriately. You will
# have to know what kind of parameters the function has, adn what the
# function of the function is.
#
# 7. From the variables file, import the accounts dictionary and the
# usernames list. Print both.

from variables import accounts, usernames

print(accounts)
print(usernames)

# 8. Import the bank_accounts module under an alias. Call the
# get_accounts function and print the accounts dictionary

import bank_accounts as bank

bank.get_accounts()

# 9. Master Question
#
# There are multiple parts to this question
# Import all the functions from the bank_accounts module

from bank_accounts import *

# Below is the information for two new clients. Add these clients to
# the accounts dictionary
#
#
# username: johnnys
# legal first name: johnathan
# legal last name: smithers
# age: 46
# balance: 3467578.37
#
#
# username: sarah87
# legal first name: sarah
# legal last name: yowletz
# age: 30
# balance: 65298.02

add_account('johnnys', 'johnathan', 'smithers', 46, 3467478.37)
add_account('sarah87', 'sarah', 'yowletz', 30, 65298.02)

# How many clients does the bank currently have? Print your result

print(get_number_of_accounts())

# What is the client number of 'johnnys'? Print your result

print(get_client_number('johnnys'))




