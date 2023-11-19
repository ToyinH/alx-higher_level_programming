#!/usr/bin/python3
"""display all values in the states table where name matches argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )

    name_search = sys.argv[4]

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (name_search, ))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
