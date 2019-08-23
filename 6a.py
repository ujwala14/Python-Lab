'''Write a python program to create a database Employee with
relevant data and display the Employees whose salary > 50000.'''

import sqlite3

con=sqlite3.connect('emp.db')
cur=con.cursor()

cur.execute('CREATE TABLE EMPLOYEE(ENO INTEGER,NAME TEXT,SALARY INTEGER)')

cur.execute("INSERT INTO EMPLOYEE VALUES(32,'TONY',300000)")
cur.execute("INSERT INTO EMPLOYEE VALUES(101,'STEVE',60000)")
cur.execute("INSERT INTO EMPLOYEE VALUES(15,'PETER',30000)")
cur.execute("INSERT INTO EMPLOYEE VALUES(129,'NATASHA',70000)")
con.commit()

cur.execute("SELECT * FROM EMPLOYEE")
E=cur.fetchall()
con.commit()
print("Employee details: ")
print("ENO\tNAME\tSALARY")
for e in E:
    print("{0}\t{1}\t{2}".format(e[0],e[1],e[2]))

cur.execute('SELECT * FROM EMPLOYEE WHERE SALARY > 50000')
E=cur.fetchall()
con.commit()
print("Employees with salary > 50000")
print("ENO\tNAME\tSALARY")
for e in E:
    print("{0}\t{1}\t{2}".format(e[0],e[1],e[2]))
