import sqlite3

# Hardcoded credentials
DB_USERNAME = "admin"
DB_PASSWORD = "password123"  # Vulnerable

def login_user(username, password):
    connection = sqlite3.connect("sample.db")
    cursor = connection.cursor()
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    connection.close()
    return user

# Example of vulnerable usage
login_user("admin' OR '1'='1", "irrelevant_password")
