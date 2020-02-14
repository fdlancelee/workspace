import xlrd
rootdir = "D:/Python/filetext/Efile/guiwaiqing-1.xls"

#打开excel文件读取数据
exce = xlrd.open_workbook(rootdir)

#获取所有sheet名字
print('所有sheet名字',exce.sheet_names())

#获取所有sheet
sheets = exce.sheets()
print('sheets',sheets)

#book.sheetby_index()来使用索引作参数来读取你想要的sheet，而索引是从0而不是从1开始的。
sheets0 = exce.sheets()[0]
print('sheets0',sheets0)

#通过sheet名获取
sheet_names = exce.sheet_by_name('对公')
print('sheet_names',sheet_names)

#获取sheet中的行数和列数
nrows = sheets0.nrows
ncols = sheets0.ncols
print('nrows',nrows,'ncols',ncols)

#获取sheet中整行或整列的数据(数组)数据从0开始
row1 = sheets0.row_values(1)
col1 = sheets0.col_values(2)
print('某行的数据',row1)
print('某列的数据',col1)

#获取sheet中某个单元格的数据
#获取第3行第1列数据
cell_A3 = sheets0.cell_value(2,0)
print('cell_A3',cell_A3)

#获取单元格数据类型
#0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
A3_type = sheets0.cell_type(2,1)
print('A3_type',A3_type)