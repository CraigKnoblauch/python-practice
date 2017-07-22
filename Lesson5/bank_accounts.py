from variables import *


# Adds a space for a new client, all arguments except 'username' are optional
def add_account(username, legal_first_name= '', legal_last_name= '', age= '', balance= ''):

    # Add the username to the list of usernames, since usernames is maintained along
    # with the accounts dictionary, the client numbers will also be maintained
    usernames.append(username)

    # Find the number of the last client in the accounts dictionary
    last_client_number = list(accounts.keys())[-1]

    # Make a number for a new client that increments the last client's number by one
    new_client_number = last_client_number + 1

    # Add a dictionary for the new client
    accounts[new_client_number] = {'username': username,
                                   'legal_first_name': legal_first_name,
                                   'legal_last_name': legal_last_name,
                                   'age': age,
                                   'balance': balance
                                   }


# A getter function to give the caller the accounts dictionary
def get_accounts():
    return accounts


# Looks for a specified client. If the client is found, their client number is returned.
# If the client is not found, an error message is printed
def get_client_number(username):
    if username.lower() in usernames:
        return usernames.index(username.lower())
    else:
        print("\nERROR: " + username + " was not found\n")


def respond_to_arg_type(arg):

    # This if statement asks if the argument is an integer.
    if isinstance(arg, int):
        # If it is, client_number is set to the argument integer.
        client_number = arg
    else:
        # If it is not, username is set to argument string, and get_client_number
        # is used to set client_number
        username = arg
        client_number = get_client_number(username.lower())

    return client_number


# This function allows the program to use either a username, or a client number
# as an argument. Either way, a dictionary for the account will be constructed
# and returned.
def get_account(username_or_client_number):

    client_number = respond_to_arg_type(username_or_client_number)

    # Construct the dictionary
    account = accounts[client_number]
    return account


def get_username(client_number):
    return accounts[client_number]['username']


# Simple getter that returns the legal first name of a client. The program can
# specify both a username or a client number.
def get_legal_first_name(username_or_client_number):
    client_number = respond_to_arg_type(username_or_client_number)
    return accounts[client_number]['legal_first_name']


# Simple getter that returns the legal last name of a client. The program can
# specify both a username or a client number.
def get_legal_last_name(username_or_client_number):
    client_number = respond_to_arg_type(username_or_client_number)
    return accounts[client_number]['legal_last_name']


# Simple getter that returns the age of a client. The program can specify both
# a username or a client number.
def get_age(username_or_client_number):
    client_number = respond_to_arg_type(username_or_client_number)
    return accounts[client_number]['age']


# Simple getter that returns the balance of a client. The program can specify
# both a username or a client number.
def get_balance(username_or_client_number):
    client_number = respond_to_arg_type(username_or_client_number)
    return accounts[client_number]['balance']


# This function grabs the first and last name of a client, concatenates them,
# and
def get_formatted_legal_name(username_or_client_number):

    client_number = respond_to_arg_type(username_or_client_number)

    name = get_legal_first_name(client_number)
    name += " "
    name += get_legal_last_name(client_number)

    return name.title()


# Populate the 'legal_first_name' value of a specified client
def set_legal_first_name(username_or_client_number, legal_first_name):

    client_number = respond_to_arg_type(username_or_client_number)

    if accounts[client_number]['legal_first_name']:
        response = input("The current legal first name is: "
                         + accounts[client_number]['legal_first_name'].title()
                         + ".\nAre you sure you want to change it? (y/n): ")

        while not (response == 'y' or response == 'n'):
            response = input("Enter a valid response (y/n): ")

        if response == 'y':
            accounts[client_number]['legal_first_name'] = legal_first_name.lower()
        else:
            print("\nThe current legal first name will remain\n")

    else:

        accounts[client_number]['legal_first_name'] = legal_first_name.lower()
        print("\nThe legal first name of "
              + get_username(client_number)
              + " has been set to "
              + legal_first_name.title()
              + ".\n")


# Populate the 'legal_last_name' value of a specified client
def set_legal_last_name(username_or_client_number, legal_last_name):
    client_number = respond_to_arg_type(username_or_client_number)

    if accounts[client_number]['legal_last_name']:
        response = input("The current legal last name is: "
                         + accounts[client_number]['legal_last_name'].title()
                         + ".\nAre you sure you want to change it? (y/n): ")

        while not (response == 'y' or response == 'n'):
            response = input("Enter a valid response (y/n): ")

        if response == 'y':
            accounts[client_number]['legal_last_name'] = legal_last_name.lower()
        else:
            print("\nThe current legal last name will remain\n")

    else:

        accounts[client_number]['legal_last_name'] = legal_last_name.lower()
        print("\nThe legal last name of "
              + get_username(client_number)
              + " has been set to "
              + legal_last_name.title()
              + ".\n")


# Populate the 'age' value of a specified client
def set_age(username_or_client_number, age):
    client_number = respond_to_arg_type(username_or_client_number)

    if accounts[client_number]['age']:
        response = input("The current age is: "
                         + str(accounts[client_number]['age'])
                         + ".\nAre you sure you want to change it? (y/n): ")

        while not (response == 'y' or response == 'n'):
            response = input("Enter a valid response (y/n): ")

        if response == 'y':
            accounts[client_number]['age'] = age
        else:
            print("\nThe current age will remain\n")

    else:

        accounts[client_number]['age'] = age
        print("\nThe age of "
              + get_username(client_number)
              + " has been set to "
              + str(age)
              + ".\n")


# Populate the 'balance' value of a specified client. Default balance is 0
def set_balance(username_or_client_number, balance= 0):
    client_number = respond_to_arg_type(username_or_client_number)

    if accounts[client_number]['balance']:
        response = input("The current balance is: "
                         + str(accounts[client_number]['balance'])
                         + ".\nAre you sure you want to change it? (y/n): ")

        while not (response == 'y' or response == 'n'):
            response = input("Enter a valid response (y/n): ")

        if response == 'y':
            accounts[client_number]['balance'] = balance
        else:
            print("\nThe current balance will remain\n")

    else:

        accounts[client_number]['balance'] = balance
        print("\nThe balance of "
              + get_username(client_number)
              + " has been set to "
              + str(balance)
              + ".\n")


# A function to give the number of clients in our database
def get_number_of_accounts():
    return len(usernames)


