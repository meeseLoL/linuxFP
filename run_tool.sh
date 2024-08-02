#!/bin/bash

# Function to display a message and run a Python script
run_python_script() {
    python mainMenu.py
}

# Function to set up the database (if not already done)
setup_database() {
    python -c "from db_connection import skeletondb; skeletondb()"
}

# Ensure the database is set up
setup_database

# Run the main menu
run_python_script
