import sqlite3


def import_data():

    conn = sqlite3.connect('/Users/kostyantynkutsenko/testdb')
    c = conn.cursor()

    c.execute("INSERT INTO tbl1 VALUES ('Hi!', 30)")
    c.execute("INSERT INTO tbl1 VALUES ('Why?', 40)")
    c.execute("DELETE FROM tbl1 WHERE two = 40")
    c.execute('SELECT * FROM tbl1')

    data = c.fetchall()
    conn.commit()
    conn.close()
    return data


print(import_data())

