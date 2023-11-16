#!/usr/bin/python3

''' This script selects all states from the database hbtn_0e_0_usa '''

import MySQLdb
import sys


if __name__ == "__main__":
    av = sys.argv
    username = av[0]
    password = av[1]
    dbname = av[2]

    db = MySQLdb.connect(user=username, password=password, database=dbname,
                         host="localhost", port=3306)

    c = db.cursor()
    c.execute("""SELECT id, name FROM states ORDER BY id;""")
