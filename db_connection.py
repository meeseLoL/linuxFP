import sqlite3

def connect_to_skeletondb():
    con = sqlite3.connect('skeletondb.db')
    return con    

def skeletondb():
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS employees (
            employee_id TEXT NOT NULL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            job_title TEXT,
            perms TEXT)''')
    con.commit()
    con.close()

def get_all_employees():
    con = sqlite3.connect('skeletondb.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    con.close()

    return rows

# Ensure the database and table are created when the module is loaded
if __name__ == "__main__":
    skeletondb()
