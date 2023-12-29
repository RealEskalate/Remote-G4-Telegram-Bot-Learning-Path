import sqlite3 as sq 



async def start_db():
    global db, cur 
    db = sq.connect('bot.db')
    cur = db.cursor()

    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS accounts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255) ,
                firstName VARCHAR(255) NOT NULL,
                LastName VARCHAR(255) NOT NULL,
                bio VARCHAR(255) NOT NULL,
                phoneNumber VARCHAR(255) NOT NULL,
                photoURL VARCHAR(255) NOT NULL
            )
        """)
        db.commit()
        print("Database table created successfully.")
    except Exception as e:
        print(f"Error creating database table: {e}")

async def update_profile(user_id, firstName, lastName, bio, phoneNumber, photoURL): 
    cur.execute(
        """
        UPDATE accounts SET firstName = ?, lastName = ?, bio = ?, phoneNumber = ?, photoURL = ? WHERE user_id = ?
        """,
        (firstName, lastName, bio, phoneNumber, photoURL, user_id)
    )
    db.commit()
    return True

async def create_profile(user_id, firstName, lastName, bio, phoneNumber, photoURL):
    try:
        status = cur.execute(
            """
            INSERT INTO accounts (user_id, firstName, lastName, bio, phoneNumber, photoURL)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (user_id, firstName, lastName, bio, phoneNumber, photoURL)
        )
        db.commit()
        print(status)
        return status
    except: 
        return {}

async def delete_profile(user_id):
    cur.execute(
        """
        DELETE FROM accounts WHERE user_id = ?
        """, 
        (user_id,)
    )
    db.commit()
    return True

async def get_profile(user_id):
    try:
        user = cur.execute("SELECT * FROM accounts WHERE user_id = :user_id", {'user_id': user_id}).fetchone()
        db.commit()
        # print("inside the db", user)
        return user
    except Exception as e:
        print(e)
        return {}


