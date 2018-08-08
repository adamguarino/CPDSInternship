import xlsxwriter

#create a new Excel file
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

#writes to a specific cell
worksheet.write('A1', 'Hello world')

workbook.close()
