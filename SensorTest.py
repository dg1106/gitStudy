from openpyxl import Workbook
wb_orig = Workbook('./abcd.xlsx')
wb_new = Workbook('./abcd2.xlsx')

sheet_orig = wb_orig.get_sheet_by_name('Sheet1')
sheet_new = wb_new.get_sheet_by_name('Sheet1')

cell_range = sheet_orig['G9':'M13']

print(cell_range)