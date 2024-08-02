#!/bin/bash

# Function to display a message and run a Python script
run_python_script() {
    python mainMenu.py
}

# Function to set up the database (if not already done)
setup_database() {
    python -c "from db_connection import skeletondb; skeletondb()"
}


# Creates a folder for the current month 'year-month'
curr_month=$(date +'%y-%m')
mkdir -p "$curr_month"
echo "Created '$curr_month' folder."

# Copies the logs.txt to the $curr_month folder with a timestamp
date +%s
cp logs.txt "$curr_month/$timestamp.txt"
echo "copied 'logs.txt' to '$curr_month'"

# Changes perms of logs.txt to owner: read and write, everyone else: read (rw-r--r--)
chmod 644 logs.txt
echo "Permissions changed"
ls -l #Lists the contents of the directors with it's permissions

# Ensure the database is set up
setup_database

# Run the main menu
run_python_script
