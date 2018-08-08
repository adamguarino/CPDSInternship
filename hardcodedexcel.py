from datetime import datetime
import xlsxwriter

#Creates an Excel file named Expenses.xlsx
workbook = xlsxwriter.Workbook('Expenses.xlsx')
worksheet = workbook.add_worksheet()

#Adds a bold format
bold = workbook.add_format({'bold':1})

#Adds a number format for any cells with money
money_format = workbook.add_format({'num_format': '$#,##0'})

#Adds a date format
date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})


#Creates bold column headers 
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Date', bold)
worksheet.write('C1', 'Cost', bold)

#Creates a tuple containing the rows to be inserted into the spreadsheet
expenses = (
    ['Rent', '2013-01-13', 1000],
    ['Gas', '2013-01-14', 100],
    ['Food', '2013-01-16', 300],
    ['Gym', '2013-01-20', 50],
    )

#Start from the first cell below the headers
row = 1
col = 0

#Iterate through the data, write it our row by row and format it
for item, date_str, cost in (expenses):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    worksheet.write_string(row, col, item)
    worksheet.write_datetime(row, col + 1, date, date_format)
    worksheet.write_number(row, col + 2, cost, money_format)
    row += 1
    
#Write a total using a formula
worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 2, '=SUM(C2:C5)', money_format)

workbook.close()
