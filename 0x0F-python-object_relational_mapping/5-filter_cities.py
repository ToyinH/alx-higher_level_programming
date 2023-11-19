#!/usr/bin/python3
""" list all states from the database """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    state_name = sys.argv[4]

    cursor = db.cursor()
    query = "SELECT cities.name FROM cities WHERE "

    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    rows = cursor.fetchall()

    cursor.close()
    db.close()
