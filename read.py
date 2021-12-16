import sqlite3
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    sql = 'SELECT * FROM topics'
    cursor.execute(sql)
    # row = cursor.fetchone()

    # print(row)
    # print(type(row))
    # print(row[1]+', '+row[2])

    rows = cursor.fetchall()
    # print(rows)

    for row in rows:
        print(row[0], row[1], row[2])
