import mysql.connector

from mysql.connector import Error

try:

    conn = mysql.connector.connect(

        host="localhost",

        user="root",

        password="mysqlroot",

        database="",

        charset=""

    )

    if conn.is_connected():

        print("Connected")

        cur = conn.cursor()

        cur.execute("SELECT VERSION()")

        print(cur.fetchone())

except Error as e:

    print("Connection error:", e)

finally:

    print("hello")

    # if conn.is_connected():

    #     conn.close()

