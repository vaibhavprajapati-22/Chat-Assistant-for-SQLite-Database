import sqlite3

DB_PATH = "company.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create Employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER,
    Hire_Date TEXT
)
""")

# Create Departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Manager TEXT
)
""")

# Insert sample data
cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", [
    (1, 'Alice', 'Sales', 50000, '2021-01-15'),
    (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
    (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
])

cursor.executemany("INSERT INTO Departments VALUES (?, ?, ?)", [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie')
])

conn.commit()
conn.close()
print("Database setup complete.")
