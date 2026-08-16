# import openpyxl

# book = openpyxl.load_workbook(r"C:\Users\hp\company.xlsx")
# sheet = book.active

# cell = sheet.cell(row=1, column=4)
# print(cell.value)  # Print the value of the cell at row 1, column 1
#-------------------------------------->
# import openpyxl

# # Load the workbook
# book = openpyxl.load_workbook(r"C:\Users\hp\company.xlsx")

# Select the active sheet
# sheet = book.active

# Write data to row 2, column 3
# sheet.cell(row=2, column=3).value = "Communication"

# # # Save the workbook
# book.save(r"C:\Users\hp\company.xlsx")

# print("Data written successfully!")

#--------------------------------------->


class Managment:
    a = 100
    b = 200
    def calculate(Addition):
        print("all  result")
manage1= Managment()
manage1.calculate()
print(manage1.a)   
print(manage1.b)     

