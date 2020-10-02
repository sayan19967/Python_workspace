import sqlite3

#preparing database connection
con = sqlite3.connect('D:\\Python files\\Python Application programming practice\\Test.db')

#prepare cursor
cursor = con.cursor()

#preparing sql statements
sql1 = 'drop table if exists employee'
sql2 = '''CREATE TABLE EMPLOYEE (
       EMPID INT(6) NOT NULL,
       NAME CHAR(20) NOT NULL,
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT
       )
       '''
#executing sql statements
##cursor.execute(sql1)
##cursor.execute(sql2)
##cursor.execute('select * from employee')

rec = (456789, 'Frodo', 45, 'M', 100000.00)
records = [

    (123456, 'John', 25, 'M', 50000.00),

    (234651, 'Juli', 35, 'F', 75000.00),

    (345121, 'Fred', 48, 'M', 125000.00),

    (562412, 'Rosy', 28, 'F', 52000.00)

    ]

sql3 = '''

       INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)

      '''
sql4 = '''select * from employee'''
##try:
###    cursor.execute(sql3, rec)
##    cursor.executemany(sql3, records)
##    con.commit()
##
##except Exception as e:
##    print(str(e))
##    con.rollback()

try:
    cursor.execute(sql4)
except Exception as e:
    print('Unable to fetch data :', str(e))

res_set = cursor.fetchall()

for res in res_set:
    print(res)

#closing connection
con.close()
