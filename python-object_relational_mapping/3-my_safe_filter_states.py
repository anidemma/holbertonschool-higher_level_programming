#!/usr/bin/python3
"""SQL Injection..."""

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
        cursor.execute("SELECT * FROM states")
    except MySQLdb.Error as e:
        print(e)
    [print(state) for state in cursor.fetchall() if state[1] == argv[4]]
    cursor.close()
    db.close()
