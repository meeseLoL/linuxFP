from datetime import datetime
import os
import sqlite3
import re

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
    while True:
        employee_id = input("Enter employee's unique id (5 alphabetic characters followed by 2 numeric characters): ")
        if re.match(r'^[A-Za-z]{5}\d{2}$', employee_id):
            break
        else:
            print("Invalid employee ID. Please try again.")
            
    while True:
        first_name = input("Enter employee's first name (alphabetic characters only): ")
        if re.match(r'^[A-Za-z]+$', first_name):
            break
        else:
            print("Invalid first name. Please try again.")
            
    while True:
        last_name = input("Enter employee's last name (alphabetic characters only): ")
        if re.match(r'^[A-Za-z]+$', last_name):
            break
        else:
            print("Invalid last name. Please try again.")
            
    while True:
        job_title = input("Enter employee's job title (alphabetic characters only): ")
        if re.match(r'^([A-Za-z]+ ?){1,4}$', job_title):
            break
        else:
            print("Invalid job title. Please try again.")
            
    while True:
        perms = input("Enter employee's permissions (numeric 1-5): ")
        if re.match(r'^[1-5]$', perms):
            break
        else:
            print("Invalid permissions. Please enter a number between 1 and 5.")
            
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute('''INSERT INTO employees (employee_id, first_name, last_name, job_title, perms) VALUES (?, ?, ?, ?, ?)''', (employee_id, first_name, last_name, job_title, perms))
    con.commit()
    con.close()
    print(f"Employee {employee_id} added successfully.")
    log_action(f"Added employee {employee_id}: {first_name} {last_name}, {job_title}, {perms}")

def modifyEmployee():
    while True:
        employee_id = input("Enter the employee ID to modify (5 alphabetic characters followed by 2 numeric characters): ")
        if re.match(r'^[A-Za-z]{5}\d{2}$', employee_id):
            break
        else:
            print("Invalid employee ID. Please try again.")
    
    while True:
        field = input("Enter the field to modify (first_name, last_name, job_title, perms): ")
        if field in ["first_name", "last_name", "job_title", "perms"]:
            break
        else:
            print("Invalid field. Please try again.")
            
    while True:
        new_value = input(f"Enter the new value for {field}: ")
        if field in ["first_name", "last_name", "job_title"]:
            if re.match(r'^[A-Za-z]+$', new_value):
                break
            else:
                print(f"Invalid {field}. Please try again.")
        elif field == "perms":
            if re.match(r'^[1-5]$', new_value):
                break
            else:
                print("Invalid permissions. Please enter a number between 1 and 5.")
    
    con = connect_to_skeletondb()
    cur = con.cursor()
    cur.execute(f'''UPDATE employees SET {field} = ? WHERE employee_id = ?''', (new_value, employee_id))
    con.commit()
    con.close()
    print(f"Employee {employee_id} updated successfully.")
    log_action(f"Modified employee {employee_id}, set {field} to {new_value}")

def deleteEmployee():
    while True:
        employee_id = input("Enter the employee ID to delete (5 alphabetic characters followed by 2 numeric characters): ")
        if re.match(r'^[A-Za-z]{5}\d{2}$', employee_id):
            break
        else:
            print("Invalid employee ID. Please try again.")
    
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
