import sqlite3
import xlsxwriter
from databaseGUI import *

workbook = xlsxwriter.Workbook('WEBCLSDES.xlsx')
worksheet = workbook.add_worksheet()

format = workbook.add_format()
format.set_align("vcenter")
worksheet.set_column(1, 1, 15)


connection = sqlite3.connect("myTable2.db")
crsr = connection.cursor()

gui = Gui()
tableName = gui.startLoop()

#Retrieves all the data row by row, stores in 'rows'
sql_command = "SELECT * FROM " + tableName + ";"
crsr.execute(sql_command)
rows = crsr.fetchall()
print(rows)

#Retrieves all the column data, stores in 'colData'
sql_command = "PRAGMA table_info(" + tableName + ");"
crsr.execute(sql_command)
colData = crsr.fetchall()
print(colData)


#Writes column names, taking them from the 1st index in colData
rowNum = 0
colNum = 0
for column in colData:
    worksheet.write(rowNum, colNum, column[1], format)
    colNum += 1
    
#Writes the rest of the table
rowNum = 1
colNum = 0
for row in rows:
    colNum = 0
    for data in row:
        worksheet.write(rowNum, colNum, data, format)
        colNum += 1
    rowNum += 1

workbook.close()





