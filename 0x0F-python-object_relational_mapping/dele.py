#!/usr/bin/python3

import MySQLdb

user='root'
passwd = 'R#7eM$9T'
datab='hbtn_0e_0_usa'

db=MySQLdb.connect(user=user, passwd=passwd, db=datab)
cur=db.cursor()
cur.execute("DELETE FROM states WHERE id >= 6")
db.commit()
cur.close()
db.close()
