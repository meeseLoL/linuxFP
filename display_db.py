#Contributors: Dann, Justin, Lloyd

import sqlite3

def display_database():
    con = sqlite3.connect('skeletondb.db')
    cur = con.cursor()
    
    cur.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    con.close()

if __name__ == "__main__":
    display_database()
