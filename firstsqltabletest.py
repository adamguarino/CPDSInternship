# Python code to demonstrate table creation and 
# insertions with SQL
 
# importing module
import sqlite3
# connecting to the database 
connection = sqlite3.connect("myTable2.db")
 
# cursor 
crsr = connection.cursor()
 
sql_command = """DROP TABLE myTable4;"""

crsr.execute(sql_command)
 
# SQL command to create a table in the database
sql_command = """CREATE TABLE myTable4 ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""
 
# execute the statement
crsr.execute(sql_command)
 
# SQL command to insert the data in the table
sql_command = """INSERT INTO myTable4 VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command)
 
# another SQL command to insert the data in the table
sql_command = """INSERT INTO myTable4 VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO myTable4 VALUES(84, "Adam", "Guarino", "M", "2018-07-02");"""
crsr.execute(sql_command)

sql_command = """SELECT * FROM myTable4;"""
crsr.execute(sql_command)
rows = crsr.fetchall()
print(rows)

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database.
connection.commit()
 
# close the connection
connection.close()