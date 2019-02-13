import win32com.client as win32
import os

path=r"D:\python\python_code\人查检查完的234个县数据\234县修改后确认表未汇交县-73个指标\234县修改后确认表未汇交县"

for file in os.listdir(path):
    filePath = os.path.join(path, file)
    #fileCount = fileCount + 1
    print(filePath)
    if file.upper().endswith(".XLS"):

        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(filePath)

        wb.SaveAs(filePath+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
        wb.Close()                               #FileFormat = 56 is for .xls extension
        excel.Application.Quit()