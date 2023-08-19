#!/usr/bin/python3

"""list all the states from  hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ = "__main__":
    """get the arguments of the 3"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]


    """connect to mysql server"""
    """mysqldb.connect() this helps in connecting to the database server"""
    db = Mysql.connect(host="localhost", port=3306, user=mysql_username, password=mysql_password, db=database_name)
    """create a cursor object to interact with mysql
    cursor object lets you execute statements, fetch results, etc"""
    cursor = db.cursor()
    cursor.execute("SELECT *FROM states ORDER BY id ASC")
    Rows = cursor.fetchall()

    for state in Rows:
        print(state)

    cursor.close()
    db.close()


