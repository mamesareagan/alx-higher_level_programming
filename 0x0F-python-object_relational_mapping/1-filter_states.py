#!/usr/bin/python3

# lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa:
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <mysql database> \

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM `states` ORDER BY `id`")
[print(i) for i in cur.fetchall() if i[1][0] == 'N']
