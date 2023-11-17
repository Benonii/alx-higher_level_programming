#!/usr/bin/python3

''' This script selects all states from the database hbtn_0e_0_usa '''

import MySQLdb
import sys


if __name__ == "__main__":
    av = sys.argv
    username = av[1]
    password = av[2]
    dbname = av[3]
    state_name = av[4]

    try:
        db = MySQLdb.connect(user=username, password=password, database=dbname,
                             host="localhost", port=3306)

        c = db.cursor()
        c.execute("SELECT cities.name\
                   FROM cities INNER JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %s ORDER BY cities.id;", (state_name,))

        rows = c.fetchall()

        print(', '.join(row[0] for row in rows))

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        if db:
            db.close()
