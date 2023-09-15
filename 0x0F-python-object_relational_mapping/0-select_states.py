#!/usr/bin/python3

'''lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys

username = sys.argv[1]
passwd = sys.argv[2]
datab = sys.argv[3]
db = MySQLdb.connect(user=username, passwd=passwd, db=datab)
cur = db.cursor()
cur.execute("SELECT * FROM `states`")
for i in cur.fetchall():
    print(i)
