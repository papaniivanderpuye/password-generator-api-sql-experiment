"""
    File Name: account_test.py
    Written By: Papa Nii Vanderpuye
    Date: 14th August 2018
"""
import sqlite3
import random
from account_generator import *


"""
    The below function clears the given database, creates 10 users and puts
    them into an sql database. Then takes the updates the password of each user
    from null to a random passowrd.
    :param db_path: path of the SQLite db file
    :param con: database connection object
    :returns: None
"""


def testing(con, db_path):
    # string commands to execute on sql database
    create_table = "CREATE TABLE  accounts(name text, email text," + \
                   "password text)"
    drop_table = "DROP TABLE IF EXISTS accounts"
    update_table = "UPDATE accounts SET password= :password WHERE name = :name"
    select_rows = "SELECT name from accounts"

    cur = con.cursor()
    cur.execute(drop_table)
    cur.execute(create_table)

    for i in range(10):
        create_user(db_path)

    cur.execute(select_rows)
    res = cur.fetchall()

    for row in res:
        name = row[0]
        password = generate_password(
            random.randint(6, 12), random.randint(1, 4))
        cur.execute(update_table, {'name': name, "password": password})
    con.commit()

    return


"""
    The below function attempts to connect to sql and run the test function,
    and throws and exception if it cannot.
"""


def main():
    db_path = "user_database.sqlite"

    try:
        con = sqlite3.connect(db_path)
        testing(con, db_path)
    except sqlite3.Error as e:
        print("Database error: % s" % e)
        return False
    except Exception as e:
        print("Exception in _query: % s" % e)
        return False
    finally:
        if con:
            con.close()
    return True
