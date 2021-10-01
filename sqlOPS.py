import mysqlconnector as c
import mysql.connector
import user
import operations as ops
def readUserInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        for col in cursor:
            print(f'''
            id ...................{col[0]}
            First Name ...........{col[1]}
            Last Name ............{col[2]}
            Age ..................{col[3]}
            Phone ................{col[4]}
            ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySql', error)

def insertUserInfo(fname, lname, age, phone):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO users (user_firstname, user_lastname, user_age, user_phone) VALUES ('{fname}', '{lname}', {age}, '{phone}')")
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySql', error)

def deleteUser(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM users WHERE user_id = {id}')
        conn.commit()
        readUserInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySql', error)

def updateUser(id, fname=None, lname=None, age=None, phone=None):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET  WHERE user_id = {id}')
        conn.commit()
        readUserInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySql', error)
        