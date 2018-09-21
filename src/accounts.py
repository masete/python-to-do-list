'''
The expected output is a console application that
you can use to manage your to do list.
It allows you to create an account and manipulate tasks

I have provided a structure for the code: FOLLOW INSTRUCTIONS
--------------------------------------------------------------
                    INSTRUCTIONS
--------------------------------------------------------------
1. Create a folder called src

2. Create the following files:
    - accounts.py
    - tasks.py
    - app.py

In the files, do the following:
'''
# --- accounts.py --
# This file contains code for managing your account

# dictionary where key is the  password and value is User
accounts = {"masete": "nichlas"}
status = ""

# Write a function adds user details to accounts
def Display_Menu():
    status = input("Are you a registered user? (Yes/No)? Press q to quit: ")
    if status == "Yes":
        login()
    elif status == "No":
        add_account()

def add_account(name, password):

     name = input("Create login name: ")
     if name in accounts:
        print("Login name already exist!")
     else:
        password = input("Create password: ")
        accounts[name] = password
        print("New User created!")
        """
        Adds the key value pair to the accounts dictionary
        """




def login(name, password):
    login_prompt()
     name = input("Enter login name: ")
     Password = input("Enter password: ")

     if name in accounts and accounts[name] == Password:
        print("Login successful!")
     else:
        print("User doesn't exist or wrong password!")

        """
        returns true if the password and corresponding name exist in the 
        accounts dicitionary
        """




