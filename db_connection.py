import sqlite3

def connect_to_skeletondb():
    con = sqlite3.connect('skeletondb.db')
    return con    

def skeletondb():
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS employees (
            employee_id TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            job_title TEXT,
            perms TEXT)''')

    con.commit()
    con.close()