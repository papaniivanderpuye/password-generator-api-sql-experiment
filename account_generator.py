import random
import sqlite3
import string
import re
import requests
from typing import List

"""
    File Name: account_generator.py
    Written By: Papa Nii Vanderpuye
    Date: 14th August 2018
"""

"""
    This is my implementation of the required coding section of the
    technical interview. I have described some sections of the function in
    order to further explain how my implementation works. However, the
    main explanation of how to run the files and what they do can be found
    on my README.md File.
"""

"""
    The function below generates a random password with given length and
    complexity

    Complexity levels:
        Complexity == 1: return a password with only lowercase chars
        Complexity ==  2: Previous level plus at least 1 digit
        Complexity ==  3: Previous levels plus at least 1 uppercase char
        Complexity ==  4: Previous levels plus at least 1 punctuation char

    :param length: number of characters
    :param complexity: complexity level
    :returns: generated password
"""


def generate_password(length: int, complexity: int) -> str:
    if(complexity < 1 or complexity > 4):
        print("Input Error: Enter valid complexity level: 1-4")
        return
    if (length < complexity):
        print("Input Error: For complexity level {}, ".format(complexity) +
              "given password length must be at least {}".format(complexity))
        return

    """
    In the code snippet below, the function first takes and adds one random
    character from each required type in the list of symbol_groups(ex lowercase
    letters, uppercase letters ) then it starts to take and add random
    characters from all the given groups. It adds all these characters to a
    list called password.
    """
    all_groups = [string.ascii_lowercase, string.digits,
                  string.ascii_uppercase,  string.punctuation]
    symbol_groups = all_groups[:complexity]  # takes only the groups needed
    password = []
    for group in symbol_groups:
        character = random.choice(group)
        password.append(character)

    for i in range(length - complexity):
        random_group = random.choice(symbol_groups)
        random_char = random.choice(random_group)
        password.append(random_char)

    random.shuffle(password)
    return ''.join(password)


"""
    The function below returns the password complexity level for a given
    password

    Complexity levels:
        Return complexity 1: If password has only lowercase chars
        Return complexity 2: Previous level condition and at least 1 digit
        Return complexity 3: Previous levels condition and at least 1
        uppercase char
        Return complexity 4: Previous levels condition and at least 1
        punctuation

    Complexity level exceptions (override previous results):
        Return complexity 2: password has length >= 8 chars and only lowercase
        chars
        Return complexity 3: password has length >= 8 chars and only lowercase
        and digits

    :param password: password
    :returns: complexity level
"""


def check_password_level(password: str) -> int:
    if(not password):
        print("Error: No password given")
        return

    """
    The code snippet below creates a list of regular expression ranges and a
    complexity variable. It then iterates through the list to check if any
    character in the given password is part of a regular expression. The
    re.search() method gives a boolean output type. This output is then
    converted to an integer(1 or 0) and then used to increment the complexity
    variable. The snippet therfore increases the complexity every time it finds
    at least one character belonging to a regular expression range.
    """
    reg_list = [r"[a-z]", r"\d", r"[A-Z]", r"[\W_]"]
    complexity = 0
    for reg in reg_list:
        password = password.replace("\\", "\\\\")
        complexity += int(re.search(reg, password) is not None)

    # increasing the complexity if the length is significantly long.
    if(complexity < 3 and len(password) > 7):
        complexity += 1

    return complexity


"""
    The function below retrieves a random user from https://randomuser.me/api/
    and persist the user (full name and email) into the given SQLite db

    :param db_path: path of the SQLite db file
    (to do: sqlite3.connect(db_path))
    :return: None
"""


def create_user(db_path: str) -> None:
    """
    The below code snippet requests the information of a random user,
    then parses through the received data to find the name and email
    """
    r = requests.get('https://randomuser.me/api/?inc=name,email')
    result = r.json()["results"][0]
    fullname = " ".join(list(result["name"].values()))
    email = result["email"]
    insert = "INSERT INTO accounts VALUES (:name,:email,:password)"

    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute(insert, {"name": fullname,
                             "email": email,
                             "password": None})
        con.commit()
    except sqlite3.Error as e:
        print("Database error: % s" % e)

    except Exception as e:
        print("Exception in _query: % s" % e)

    finally:
        if con:
            con.close()

    return
