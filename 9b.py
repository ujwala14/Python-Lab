'''Hospital'''

import sqlite3

con=sqlite3.connect('hospital.db')
cur=con.cursor()

cur.execute('CREATE TABLE HOSPITAL(HID INTERGER,HNAME TEXT,BCOUNT INTERGER)')
con.commit()

cur.execute("INSERT INTO HOSPITAL VALUES(1,'MAYO',200)")
cur.execute("INSERT INTO HOSPITAL VALUES(2,'CLEVELAND',400)")
cur.execute("INSERT INTO HOSPITAL VALUES(3,'JOHN HOPKINS',1000)")
cur.execute("INSERT INTO HOSPITAL VALUES(4,'UCLA',1500)")
con.commit()

cur.execute("SELECT * FROM HOSPITAL")
print(cur.fetchall())
con.commit()

cur.execute("UPDATE HOSPITAL SET BCOUNT=100 WHERE HID=1")
cur.execute("DELETE FROM HOSPITAL WHERE HID=3")
con.commit()

cur.execute("SELECT * FROM HOSPITAL")
print(cur.fetchall())
con.commit()
