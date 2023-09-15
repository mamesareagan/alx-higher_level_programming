#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
if __name__ == "__main__":
    import sys
    import MySQLdb

    usr = sys.argv[1]
    pas = sys.argv[2]
    dtb = sys.argv[3]
    db = MySQLdb.connect(user=usr, passwd=pas, db=dtb)
    c = db.cursor()
    c.execute("SELECT * FROM `states`ORDER BY `id`")
    [print(state) for state in c.fetchall()]
