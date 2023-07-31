from IPython.lib.pretty import datetime
import openpyxl

# Specify the path to your Excel file
excel_file = './sample_data/course data.xlsx'

# Load the workbook
workbook = openpyxl.load_workbook(excel_file)

# Select the first sheet (you can specify the sheet name or index)
sheet = workbook.active


# Iterate over cells and print the cell values
for row in sheet.iter_rows():
    for cell in row:
        if(cell.column==1):
          print(str(cell.value)+")")
        elif(cell.column==2):
          print("Course: "+cell.value)
        elif(cell.column==3):
          print("Place: "+cell.value)
        elif(cell.column==4):
            date=str(cell.value).split("-")[::-1][1:]
            if(len(date)>0):
              print("Date Taken: "+date[0]+"/"+date[1])
        elif(cell.column==5):
          print("Textbooks: "+cell.value)
        elif(cell.column==6):
          print("Grade: "+cell.value)