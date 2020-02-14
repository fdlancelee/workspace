import xlrd
rootdir = "D:/Python/filetext/Efile/guiwaiqing-1.xls"

#打开excel文件读取数据
#读取文件的时候需要将formatting_info参数设置为True，默认是False
exce = xlrd.open_workbook(rootdir,formatting_info=True)

#book.sheetby_index()来使用索引作参数来读取你想要的sheet，而索引是从0而不是从1开始的。
sheets0 = exce.sheets()[0]
print('sheets0',sheets0)
sheets1 = exce.sheetsheet_names = exce.sheet_by_name('对公')
sheets3 = exce.sheetsheet_names = exce.sheet_by_name('test')
sheets4 = exce.sheetsheet_names = exce.sheet_by_name('date')
print('sheets1',sheets1)

#获取sheet中的行数和列数
nrows = sheets0.nrows
ncols = sheets0.ncols
print('nrows',nrows,'ncols',ncols)

'''
#测试打印使用for来做
#行循环
for i in range(nrows):
    for j in range(ncols):
        print(sheets1.cell(i,j).value)
'''
#mergedcells返回的这四个参数的含义是：(row,rowrange,col,colrange),
#其中[row,rowrange)包括row,不包括rowrange,col也是一样，即(1, 3, 4, 5)的含义是：第1到2行（不包括3）列从下标4开始，到第四列（不包含5）
# (1, 3, 11, 12)第1到2行（不包括3）列从下标11开始，到第11列（不包含12），返回顺序是按照excl处理的顺序
print(sheets3.merged_cells)
#获取合并单元格的值
def row_col(sheet):
    merge = []
    print('merge:',merge)
    for(row,row_range,col,col_range) in sheet.merged_cells:
        merge.append([row,col])#append是在表末尾添加一个字段
        print('merge:',merge)
    for index in merge:
        print('合并单元格的值:',sheet.cell(index[0],index[1]).value)
row_col(sheets3)


#日期格式
print('格式类型',sheets4.cell_type(0,0)) #格式类型
print('转换成日期格式',xlrd.xldate_as_datetime(sheets4.cell(0,0).value,0)) #转换成日期格式
print('转换成元组',xlrd.xldate_as_tuple(sheets4.cell(0,0).value,0)) #转换成日期格式
#print(xlrd.xldate_as_datetime(sheets4.cell(0,1).value,0)) #转换成日期格式