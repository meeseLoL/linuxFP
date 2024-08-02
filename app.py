from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from employees import addEmployee, modifyEmployee, deleteEmployee, display_database, viewLogs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        job_title = request.form['job_title']
        perms = request.form['perms']
        addEmployee(employee_id, first_name, last_name, job_title, perms)
        return redirect(url_for('home'))
    return render_template('addEmployee.html')

@app.route('/modify', methods=['GET', 'POST'])
def modify_employee():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        field = request.form['field']
        new_value = request.form['new_value']
        modifyEmployee(employee_id, field, new_value)
        return redirect(url_for('home'))
    return render_template('modify.html')

@app.route('/delete')
def display():
    return display_database()

@app.route('/logs')
def logs():
    return viewLogs()

if __name__ == '__main__':
    app.run(debug=True)