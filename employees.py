import sqlite3

con = sqlite3.connect('skeletondb.db')

cur = con.cursor()

def deleteEmployeesTable():
    cur.execute('DROP TABLE IF EXISTS employees')
    con.commit()

deleteEmployeesTable()

cur.execute('''CREATE TABLE IF NOT EXISTS employees (
        employee_id TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        job_title TEXT,
        perms TEXT)''')

con.commit()

def addEmployee(employee_id, first_name, last_name, job_title, perms):
    cur.execute('''INSERT INTO employees (employee_id, first_name, last_name, job_title, perms) VALUES (?, ?, ?, ?, ?)''', (employee_id, first_name, last_name, job_title, perms))
    con.commit()


def userInput():
    employee_id = input("Enter employee's unique id: ")
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    job_title = input("Enter employee's job title: ")
    perms = input("Employee's permissions: ")
    addEmployee(employee_id, first_name, last_name, job_title, perms)

userInput()

def fetchAllEmployees():
    cur.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    for row in rows:
        print(row)

fetchAllEmployees()

con.close()