from flask import Flask, request, render_template, redirect, url_for
from db_connection import get_all_employees
import sqlite3


app = Flask(__name__)

def get_skeletondb():
    con = sqlite3.connect('skeletondb.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    con.close()


@app.route('/')
def home():
    data = get_all_employees()
    return render_template('display_db.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)