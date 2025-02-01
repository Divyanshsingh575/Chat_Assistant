# Chat Assistant 🤖 


## Introduction
Welcome to the Chat Assistant! This is a simple Chat Assistant built using Flask and SQLite. It allows users to interact with an employee database using natural language queries. The assistant understands and responds to common queries related to employees, departments, managers, and salaries.

![Chat Assistant Screen](chat_assisment/assets/Forntpage.png)

## Features ✨
💼 Fetch a list of employees from a specific department.
👩‍💼 Find out who the manager of a department is.
📅 Get a list of employees hired after a certain date.
💰 Calculate the total salary expense for a department.
## Technologies Used ⚙️
Flask: Web framework for handling HTTP requests.
SQLite: Lightweight database for storing employee and department data.
Regular Expressions: For processing and extracting relevant parts of user queries.
## Installation and Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Divyanshsingh575/Chat_Assistant.git
   cd Chat_Assistant
   ```
2. Install dependencies:
   ```sh
   pip install flask
   ```
3. Create an SQLite database named `chat_assistant.db` and set up the required tables:
   ```sql
   CREATE TABLE Employees (
       ID INTEGER PRIMARY KEY AUTOINCREMENT,
       Name TEXT,
       Department TEXT,
       Hire_Date TEXT,
       Salary INTEGER
   );
   
   CREATE TABLE Departments (
       ID INTEGER PRIMARY KEY AUTOINCREMENT,
       Name TEXT,
       Manager TEXT
   );
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. 🖥️ The server should start running at http://127.0.0.1:5000/. 🎉

## API Usage 🔧
The `/query` endpoint accepts a JSON payload with a query string. Example request:
```json
{
    "query": "Show me all employees in the Sales department"
}
```
Example response:
```json
{
    "employees": ["Alice", "Bob"]
}
```

## Future Improvements 🌱
🧠 Add more complex query support (e.g., filtering by multiple parameters).
🤖 Improve NLP capabilities for better query understanding.
🎨 Create a frontend UI for a more interactive user experience.

## Contributing 🤝
Feel free to contribute by raising issues or submitting pull requests! 🙌

## License 📜
This project is open-source and available under the MIT License. 🎉
