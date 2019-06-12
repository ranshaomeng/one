import win32com.client as win32
import os

path=r"D:\2019年土地承包处\农村承包地确权登记表（全国）\2681+157个县的结果20190102\20190102统计-数据\汇交2681汇总表（省级+县级）\承包地确权数据确认表--省级"
for file1 in os.listdir(path):
    filePath1 = os.path.join(path, file1)

    for file in os.listdir(filePath1):
        filePath = os.path.join(filePath1, file)
        #fileCount = fileCount + 1
        print(filePath)
        if file.upper().endswith(".XLS"):

            excel = win32.gencache.EnsureDispatch('Excel.Application')
            wb = excel.Workbooks.Open(filePath)

            wb.SaveAs(filePath+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
            wb.Close()                               #FileFormat = 56 is for .xls extension
            excel.Application.Quit()