import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="pdfs"
    )

    return conn

# cursor = conn.cursor()

# cursor.execute("USE pdfs;")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS documents(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     paragraph TEXT
# )
# """)

# conn.commit()
# conn.close()

# print("Database Created Successfully")