📌 Overview
This is a desktop-based Employee Management System developed using Python's Tkinter library for the graphical user interface and MySQL for the backend database. The system allows users to perform basic CRUD operations: Add, Edit, Promote, Remove, and Display employee records in a user-friendly GUI format.

🎯 Features
Add new employee records

Remove existing employees

Edit employee information (name, post, salary)

Promote employees by increasing their salary

Display all employees in a tabular format

Real-time updates to the MySQL database

Simple, clean, and intuitive GUI

🛠️ Technologies Used
Frontend: Tkinter (Python GUI)

Backend: MySQL (Database)

Programming Language: Python 3

Other Libraries: mysql.connector, tkinter.ttk

🧱 Database Schema
Make sure to create the following schema before running the application:

sql
CREATE DATABASE emp;

USE emp;

CREATE TABLE employees (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    post VARCHAR(50),
    salary FLOAT
);
🚀 How to Run the Project
1. 🛠 Prerequisites
Python 3.x installed

MySQL Server running locally

mysql-connector-python library:

bash
pip install mysql-connector-python
2. 🔧 Set Up
Update the database connection in the code if needed:

python
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="emp"
)
3. ▶️ Run the App
Run the Python file:

bash
python "employee management system GUI.py"
🖼️ GUI Components
Input Fields: ID, Name, Post, Salary

Buttons: Add, Remove, Promote, Edit, Display, Exit

Table View: Displays employee records in rows and columns

📈 Output
Interactive Tkinter window with input fields and buttons

Table of employees with live updates

Popup messages for success, error, and warnings

✍️ Author
Satvik Arun
Postgraduate in Data Science | Machine Learning Engineer
