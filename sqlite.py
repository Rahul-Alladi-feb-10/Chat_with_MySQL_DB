import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Amar','DS','A',90)''')
cursor.execute('''Insert Into STUDENT values('Akbar','CS','B',100)''')
cursor.execute('''Insert Into STUDENT values('Anthony','DS','A',86)''')
cursor.execute('''Insert Into STUDENT values('Goutham','Devops','A',50)''')
cursor.execute('''Insert Into STUDENT values('Mahesh','DS','A',90)''')

print("the inserted recors are")
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()