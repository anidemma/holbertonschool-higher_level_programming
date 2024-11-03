#!/usr/bin/python3
"""Filter states"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY id")
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for row in rows:
        if row[1][0] == 'N':
            print(row)
