from mysql.connector.errors import OperationalError
import mysql.connector

from database.models.user_model import User  # Import the User class from the models package

# Rest of the code remains unchanged
# Establish the connection
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LibanwithGod@2024",
    database="Liban"
)

if cnx.is_connected():
    print("Successfully connected to the database") 

# Register a new user
import mysql.connector
def register_user(**kwargs):
    try:
        # Establish the connection
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LibanwithGod@2024",
            database="Liban"
        )

        cursor = cnx.cursor()
        # Create the 'users' table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INT, first_name VARCHAR(255), last_name VARCHAR(255), occupation VARCHAR(255), phone_number VARCHAR(255), photo_id VARCHAR(255))")

        query = "INSERT INTO users (user_id, first_name, last_name, occupation, phone_number, photo_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (kwargs.get('user_id'), kwargs.get('first_name'), kwargs.get('last_name'), kwargs.get('occupation'), kwargs.get('phone_number'), kwargs.get('photo_id'))
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()

        # Return the user object
       
        user = User(
            user_id=kwargs.get('user_id'),
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'),
            occupation=kwargs.get('occupation'),
            phone_number=kwargs.get('phone_number'),
            photo_id=kwargs.get('photo_id')
        )
            
        
        return user
    except OperationalError:
        raise Exception("MySQL Connection not available.")

# Get all users registered so far
def get_all_users():
    cursor = cnx.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Get one user by their ID
def get_user_by_id(user_id):
    cursor = cnx.cursor()
    query = "SELECT * FROM users WHERE user_id = %s"
    values = (user_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    return result

# Filter users by name
def filter_users_by_name(name):
    cursor = cnx.cursor()
    query = "SELECT * FROM users WHERE fname LIKE %s OR lname LIKE %s"
    values = (f"%{name}%", f"%{name}%")
    cursor.execute(query, values)
    result = cursor.fetchall()
    cursor.close()
    return result

# Update one user by their ID
def update_user_by_id(user_id, new_fname):
    cursor = cnx.cursor()
    query = "UPDATE users SET fname = %s WHERE id = %s"
    values = (new_fname, user_id)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()

# Delete one user by their ID
def delete_user_by_id(user_id):
    cursor = cnx.cursor()
    query = "DELETE FROM users WHERE id = %s"
    values = (user_id,)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()






# Close the connection
cnx.close()
