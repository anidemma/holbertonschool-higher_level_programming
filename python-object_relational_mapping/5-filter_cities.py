#!/usr/bin/python3
"""All cities by state"""

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
    cursor.execute(
        'SELECT cities.id, cities.name, states.name '
        'FROM cities '
        'INNER JOIN states ON cities.state_id = states.id '
        'ORDER BY cities.id'
    )

    print(', '.join(c[1] for c in cursor.fetchall() if c[2] == argv[4]))

    cursor.close()
    db.close()
