from openpyxl import Workbook, load_workbook

workbook = load_workbook("..\EmployeeSampleData\EmployeeSampleData.xlsx")
# we can pass read_only or data_only as 2 boolean arguments to load_workbook function
# read_only -> allows to open the spreadsheet in a read only mode. Useful in case of large data excel sheets
# data_only -> ignores the formula and insteads load only the resulting value

print(workbook.sheetnames) # returns a list of sheets in the spreadsheet

sheet = workbook.active
print(sheet.title) # returns the active sheet title in spreadsheet4

print(sheet["A1"].value) # value returns the content of cell in sheet
# Another way to access a cell of sheet is using cell(row = value1, column = value2) function passing the row and column valuespr
print(f"{sheet.cell(row=1, column=2).value} : {sheet.cell(row=5, column=2).value}")

# To access the cell objects for a given column or set of columns 
print(sheet["A"]) # returns all cell objects for column A. The returned data structure is a tuple with length equal to number of cells under column A

print(sheet["A:C"]) # returns all the cell objects for columns A to C. Returned data structure is a tuple of tuples. Where each tuple inside the outer tuple is collection of cell objects for that column

print(sheet[5]) # returns list of cell objects for row number 5
print(sheet[5:7]) # returns list of cell objects for row number 5 to 7

# The above approach to access the cell objects return us the cell objects. In order to access the value we have to use a for loop.
for singlecell in sheet[5]:
    print(singlecell.value)


""" better way is to use the iter_rows() and iter_cols(). 
We have to pass 4 parameters min_row, max_row, min_col, max_col for both functions. This will return the cell objects in a tuple.
iter_rows() returns the tuple of cell objects row wise whereas iter_cols() returns the tuple of cell objects column wise
we can pass also values_only boolean parameter to return the value instead of cell object. """

for cells in sheet.iter_rows(min_row=2,
                            max_row=5,
                            min_col=2,
                            max_col=3):
    for cellVal in cells:
        print(cellVal.value, end=" ")
    print()

print()

for cells in sheet.iter_cols(min_row=2,
                            max_row=5,
                            min_col=2,
                            max_col=3):
    for cellVal in cells:
        print(cellVal.value, end=" ")
    print()

print()

""" instead of using iter_rows we can also rows which directly gives us the tuple of cell objects row wise"""

for row in sheet.rows:
    print(row)