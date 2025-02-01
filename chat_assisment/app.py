from flask import Flask, request, jsonify, render_template
import sqlite3
import datetime

app = Flask(__name__)


def connect_db():
    return sqlite3.connect("chat_assistant.db")


def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    

@app.route("/")
def home():
    return render_template("index.html") 


@app.route("/query", methods=["POST"])
def query_database():
    data = request.json
    user_query = data.get("query", "").lower().strip()  

    if not user_query:
        return jsonify({"message": "Query cannot be empty. Please enter a valid request."})

    conn = connect_db()
    cursor = conn.cursor()
    response = {"message": "I didn't understand your query."}

    try:
        # Query 1:
        if "show me all employees in the" in user_query and "department" in user_query:
            department = user_query.split("show me all employees in the ")[1].split(" department")[0].strip()
            cursor.execute("SELECT Name FROM Employees WHERE LOWER(Department) = ?", (department.lower(),))  
            employees = [row[0] for row in cursor.fetchall()]
            response = {"employees": employees} if employees else {"message": f"No employees found in the {department} department."}

        # Query 2:
        elif "who is the manager of the" in user_query and "department" in user_query:
            department = user_query.split("who is the manager of the ")[1].split(" department")[0].strip()
            cursor.execute("SELECT Manager FROM Departments WHERE LOWER(Name) = ?", (department.lower(),))  # Ensure case insensitivity
            manager = cursor.fetchone()
            response = {"manager": manager[0]} if manager else {"message": f"Department {department} not found."}
            

        # Query 3: 
        elif "list all employees hired after" in user_query:
            date_str = user_query.split("list all employees hired after ")[1].strip()
            print(f"Received date string: '{date_str}'")
            date_str = ''.join(c for c in date_str if c.isdigit() or c == '-')
            if not is_valid_date(date_str):
                response = {"message": "Invalid date format. Please use YYYY-MM-DD."}
            else:
                cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date_str,))
                employees = [row[0] for row in cursor.fetchall()]
                response = {"employees": employees} if employees else {"message": f"No employees found hired after {date_str}."}

                
        # Query 4
        elif "what is the total salary expense for the" in user_query and "department" in user_query:
            department = user_query.split("what is the total salary expense for the ")[1].split(" department")[0].strip()
            cursor.execute("SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) = ?", (department.lower(),))  
            total_salary = cursor.fetchone()[0]
            response = {"total_salary": total_salary} if total_salary else {"message": f"No salary data found for {department} department."}
        return jsonify(response)
    
    except Exception as e:
        response = {"message": f"An error occurred: {str(e)}"}
    finally:
        conn.close()
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
