import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="ypur sql host name",
        user="username",
        password="ypur password",
        database="database name"
    )

    return conn

