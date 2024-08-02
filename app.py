from flask import Flask, request, render_template, redirect, url_for
from db_connection import get_all_employees

app = Flask(__name__)

@app.route('/')
def home():
    data = get_all_employees() #pulls all employee data from the database
    return render_template('display_db.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)