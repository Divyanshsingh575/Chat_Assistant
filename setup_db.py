import sqlite3  # Import SQLite library

# Step 1: Connect to SQLite (Creates the file if not exists)
conn = sqlite3.connect("chat_assistant.db")
cursor = conn.cursor()

# Step 2: Create Employees Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Hire_Date TEXT NOT NULL
)
""")

# Step 3: Create Departments Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Manager TEXT NOT NULL
)
""")

# Step 4: Insert Sample Data into Employees Table
cursor.executemany("INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?, ?)", [
    (1, "Alice", "Sales", 50000, "2021-01-15"),
    (2, "Bob", "Engineering", 70000, "2020-06-10"),
    (3, "Charlie", "Marketing", 60000, "2022-03-20")
])

# Step 5: Insert Sample Data into Departments Table
cursor.executemany("INSERT INTO Departments (ID, Name, Manager) VALUES (?, ?, ?)", [
    (1, "Sales", "Alice"),
    (2, "Engineering", "Bob"),
    (3, "Marketing", "Charlie")
])

# Step 6: Commit changes and close the connection
conn.commit()
conn.close()

print("Database created successfully!")
