from datetime import datetime
import os
import sqlite3

def connect_to_skeletondb():
    con = sqlite3.connect('skeletondb.db')
    return con    

def log_action(action):
    with open('logs.txt', 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{timestamp} - {action}\n")

def display_database():
    con = connect_to_skeletondb()
    cur = con.cursor()
    
    cur.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    con.close()
    log_action("Displayed database")

def addEmployee():
    employee_id = input("Enter employee's unique id: ")
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    job_title = input("Enter employee's job title: ")
    perms = input("Employee's permissions: ")
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute('''INSERT INTO employees (employee_id, first_name, last_name, job_title, perms) VALUES (?, ?, ?, ?, ?)''', (employee_id, first_name, last_name, job_title, perms))
    con.commit()
    con.close()
    print(f"Employee {employee_id} added successfully.")
    log_action(f"Added employee {employee_id}: {first_name} {last_name}, {job_title}, {perms}")

def modifyEmployee():
    employee_id = input("Enter the employee ID to modify: ")
    field = input("Enter the field to modify (first_name, last_name, job_title, perms): ")
    new_value = input(f"Enter the new value for {field}: ")
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute(f'''UPDATE employees SET {field} = ? WHERE employee_id = ?''', (new_value, employee_id))
    con.commit()
    con.close()
    print(f"Employee {employee_id} updated successfully.")
    log_action(f"Modified employee {employee_id}, set {field} to {new_value}")

def deleteEmployee():
    employee_id = input("Enter the employee ID to delete: ")
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute('''DELETE FROM employees WHERE employee_id = ?''', (employee_id,))
    con.commit()
    con.close()
    print(f"Employee {employee_id} deleted successfully.")
    log_action(f"Deleted employee {employee_id}")

def viewLogs():
    # Assuming logs are stored in a file named 'logs.txt'
    if os.path.exists('logs.txt'):
        with open('logs.txt', 'r') as file:
            print(file.read())
    else:
        print("No logs found.")
    log_action("Viewed logs")
