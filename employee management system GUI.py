import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

# Database connection
def create_connection():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shauny@123",
            database="emp"
        )
        return con
    except Error as e:
        messagebox.showerror("Connection Error", f"Error: {e}")
        return None

con = create_connection()
cursor = con.cursor()

# Function to check if an employee exists
def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'
    cursor.execute(sql, (employee_id,))
    return cursor.fetchone() is not None

# Function to add an employee
def add_employee():
    Id = entry_id.get()
    Name = entry_name.get()
    Post = entry_post.get()
    try:
        Salary = float(entry_salary.get())
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for salary. Please enter a numeric value.")
        return

    if check_employee(Id):
        messagebox.showwarning("Duplicate Entry", "Employee already exists. Please try again.")
        return

    sql = 'INSERT INTO employees (id, name, post, salary) VALUES (%s, %s, %s, %s)'
    data = (Id, Name, Post, Salary)
    try:
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Employee Added Successfully")
        display_employees()  # Update table after adding
    except Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        con.rollback()

# Function to remove an employee
def remove_employee():
    Id = entry_id.get()
    if not check_employee(Id):
        messagebox.showwarning("Not Found", "Employee does not exist. Please try again.")
        return

    sql = 'DELETE FROM employees WHERE id=%s'
    data = (Id,)
    try:
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Employee Removed Successfully")
        display_employees()  # Update table after removing
    except Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        con.rollback()

# Function to promote an employee
def promote_employee():
    Id = entry_id.get()
    if not check_employee(Id):
        messagebox.showwarning("Not Found", "Employee does not exist. Please try again.")
        return

    try:
        Amount = float(entry_salary.get())
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for salary increase. Please enter a numeric value.")
        return

    try:
        sql_select = 'SELECT salary FROM employees WHERE id=%s'
        cursor.execute(sql_select, (Id,))
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + Amount

        sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
        cursor.execute(sql_update, (new_salary, Id))
        con.commit()
        messagebox.showinfo("Success", "Employee Promoted Successfully")
        display_employees()  # Update table after promotion
    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        con.rollback()

# Function to edit employee details
def edit_employee():
    Id = entry_id.get()
    if not check_employee(Id):
        messagebox.showwarning("Not Found", "Employee does not exist. Please try again.")
        return

    Name = entry_name.get()
    Post = entry_post.get()

    try:
        Salary = float(entry_salary.get())
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for salary. Please enter a numeric value.")
        return

    sql_update = 'UPDATE employees SET name=%s, post=%s, salary=%s WHERE id=%s'
    data = (Name, Post, Salary, Id)
    try:
        cursor.execute(sql_update, data)
        con.commit()
        messagebox.showinfo("Success", "Employee Details Updated Successfully")
        display_employees()  # Update table after editing
    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        con.rollback()

# Function to display all employees in a table
def display_employees():
    for row in tree.get_children():
        tree.delete(row)

    try:
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        if employees:
            for employee in employees:
                tree.insert("", "end", values=employee)
        else:
            messagebox.showinfo("No Data", "No employees found.")
    except Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# GUI Setup
root = tk.Tk()
root.title("Employee Management System")
root.geometry("800x600")

# Employee ID
tk.Label(root, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

# Employee Name
tk.Label(root, text="Employee Name").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

# Employee Post
tk.Label(root, text="Employee Post").grid(row=2, column=0, padx=10, pady=5)
entry_post = tk.Entry(root)
entry_post.grid(row=2, column=1, padx=10, pady=5)

# Employee Salary
tk.Label(root, text="Employee Salary").grid(row=3, column=0, padx=10, pady=5)
entry_salary = tk.Entry(root)
entry_salary.grid(row=3, column=1, padx=10, pady=5)

# Buttons for operations
tk.Button(root, text="Add Employee", command=add_employee).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Remove Employee", command=remove_employee).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Promote Employee", command=promote_employee).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Edit Employee", command=edit_employee).grid(row=5, column=1, padx=10, pady=10)

# Treeview for displaying employees in table format
columns = ("ID", "Name", "Post", "Salary")
tree = ttk.Treeview(root, columns=columns, show='headings', height=10)
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Setting column headings
tree.heading("ID", text="Employee ID")
tree.heading("Name", text="Employee Name")
tree.heading("Post", text="Employee Post")
tree.heading("Salary", text="Employee Salary")

# Set column widths
tree.column("ID", width=100)
tree.column("Name", width=200)
tree.column("Post", width=150)
tree.column("Salary", width=100)

# Display Employees button to refresh the table
tk.Button(root, text="Display Employees", command=display_employees).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Exit Button
tk.Button(root, text="Exit", command=root.quit).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

# Close the database connection when the app is closed
cursor.close()
con.close()
