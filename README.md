# Introduction
This file aims to further explain my solution files for creating a user account with a generated password, and saving it in a database.
I used Python 3.6.5 to run my code. In the following paragraphs, I will talk about the execution of my files and the functions in my files. `requirements.txt` contains the name of the module you may have to install for my program to work.

## How to run
My solutions are `account_generator.py`, `user_create.py`, `password_unit_test.py` and `user_create_unit_test.py`. The solutions can be run like this:

`$ python3.6 -m unittest password_unit_test.Test`
`$ python3.6 -m unittest user_create_unit_test.Test`

Where `password_unit_test.Test` tests my implementation of the **generate_password** and **check_password_level** functions inside `account_generator.py`, and `user_create_unit_test.Test` tests my implementation of **create_user** in the same file, using a helper script called 'user_create.py' and 'python3.6' is a python version of 3.6 or higher that is used.

# account_generator.py
This python script contains all the functions I created and tested

## generate_password
The function takes in the length of a password and the complexity and then returns a random password with a given complexity. It creates list of all character/symbol groups needed to create the passwords. It returns the needed password, or `None` if the parameters given are wrong.


## check_password_level
This function returns the complexity level of a given password or `None` if no password is given. It creates a list of regular expression ranges and a complexity variable. It then iterates through the list to check if any character in the given password is part of a regular expression. It increases the level any time it finds a character belonging to a regular expression group that has not been already used.

## create_user
This function creates a user and then stores it in a given SQL database. It requests the information of a random user using an API, then parses through the received data to find the name and email then persists the information into a the SQL database, as a new user account entry with no password.

# password_unit_test.py
This is my unit test script to check the **generate_password** and **check_password_level** functions in `account_generator.py` This function tests password lengths in n range -2 to 50.

# user_create.py
This is my script to run the **create_user** function in `account_generator.py`.

## testing
This function clears the given database, creates 10 users and puts them into an sql database. Then takes the updates the password of each user from null to a random password.

## main
This function attempts to connect to sql and run the test function, and throws and exception if it cannot.

# user_create_unit_test.py
This is my unit test script to check the **main** and **testing** functions in `user_create.py` This function runs the main function and makes sure there are no errors in retrieving and updating the sql data.


# Conclusion
That is all to say about the files I submitted. I really enjoyed this coding assignment. Thank you for the opportunity!
