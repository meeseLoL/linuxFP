from db_connection import connect_to_skeletondb

def addEmployee(employee_id, first_name, last_name, job_title, perms):
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute('''INSERT INTO employees (employee_id, first_name, last_name, job_title, perms) VALUES (?, ?, ?, ?, ?)''', (employee_id, first_name, last_name, job_title, perms))
    con.commit()
    con.close()


def userInput():
    employee_id = input("Enter employee's unique id: ")
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    job_title = input("Enter employee's job title: ")
    perms = input("Employee's permissions: ")
    addEmployee(employee_id, first_name, last_name, job_title, perms)

def fetch_all_employees():
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    con.close()
    return rows

userInput()

employees = fetch_all_employees()
for employee in employees:
    print(employee)