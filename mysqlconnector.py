import mysql.connector, os
from mysql.connector import connect

def returnConnection():
    conn = connect(
        host = "mysqldatabase.cz2okqpkpjg5.us-east-1.rds.amazonaws.com",
        user = "admin",
        password = "qazQAZ123!",
        database = "myACIdb"
    )
    return conn