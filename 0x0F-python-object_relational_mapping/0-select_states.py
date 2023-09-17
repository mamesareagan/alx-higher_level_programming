#!/usr/bin/python3

# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys 
import MySQLdb

usr = sys.argv[1]
pas = sys.argv[2]
dtb = sys.argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=usr, passwd=pas, db=dtb)
    c = db.cursor()
    c.execute("SELECT * FROM `states`ORDER BY `id` ASC")
    for state in c.fetchall():
        print(state)
    db.commit()
    c.close()
    db.close()
