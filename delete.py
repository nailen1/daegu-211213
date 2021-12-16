import sqlite3
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    id = input('삭제할 행의 아이디를 알려주세요: ')
    sql = 'DELETE FROM topics WHERE id = ?'
    cursor.execute(sql, (id,))
    # get arg as tuple ( ,)
