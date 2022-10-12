import mysql.connector

class Base:

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="shows"
    )

    cursor = db.cursor()
    
    