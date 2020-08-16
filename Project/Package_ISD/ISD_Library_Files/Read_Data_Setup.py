
#@author: Bharath HS

import os
#import pyodbc
import xlrd
import csv
#import xlsxwriter
from pathlib import Path
#from selenium.webdriver.common.actions.interaction import NONE

class Read_Excel():   
    
    def __init__(self):
        #self.testc_arg = testc_arg
        #self.test_sheet_arg = test_sheet_arg
        #self.column_arg = column_arg
        self.fields = [] 
        self.rows = [] 
        self.data = {}
        self.list_sheet = []

    def csv_from_excel(self,XL_path):
        workBook = xlrd.open_workbook(XL_path+"Data_Setup.xls")
        sheet_names = workBook.sheet_names()
        list_sheet = []
        sheet_name = {}
        lenth = len(sheet_names)
        #print(lenth)

        for i in range(0,lenth):
            sheet_name[sheet_names[i]]=XL_path+sheet_names[i]+".csv"
            sheet =  workBook.sheet_by_name(sheet_names[i])
            list_sheet.append(sheet)
            yourcsvFile = open(XL_path+sheet_names[i]+".csv",'w')
            wr = csv.writer(yourcsvFile, quoting=csv.QUOTE_ALL)
            total_row = list_sheet[i].ncols
            
            for rownum in range(list_sheet[i].nrows):
                wr.writerow(list_sheet[i].row_values(rownum))

        yourcsvFile.close()
        
        return sheet_name
    
    def Check_Test_Case_Arg(self,excel_path,testc_arg):
        filename = excel_path
        self.testc_arg = testc_arg  
        # initializing the titles and rows list 
        fields = [] 
        rows = [] 
        data = {}
        counter = 0
        # reading csv file 
        with open(filename, 'r') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
              
            # extracting field names through first row 
            fields = next(csvreader) 

            #print(csvreader)
            # extracting each data row one by one 
            for row in csvreader:
                #print(row) 
                if not len(row)==0:
                    rows.append(row) 
          
            # get total number of rows 
            #print("Total no. of rows: %d"%(csvreader.line_num)) 
          
        # #printing the field names 
        #print('Field names are:' + ', '.join(field for field in fields)) 
        #print(fields)
        #print(rows)

        for row in rows: 
            # parsing each column of a row 
            #print(row)
            if row[2]==str(self.testc_arg):
                if row[5]==str("Y"):
                    return True
                else:
                    return False
        
    def Get_ExcelData(self,excel_path,testc_arg):
        filename = excel_path
        self.testc_arg = testc_arg  
        # initializing the titles and rows list 
        fields = [] 
        rows = [] 
        data = {}
        counter = 0
        # reading csv file 
        with open(filename, 'r') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
              
            # extracting field names through first row 
            fields = next(csvreader) 

            #print(csvreader)
            # extracting each data row one by one 
            for row in csvreader:
                #print(row) 
                if not len(row)==0:
                    rows.append(row) 
          
            # get total number of rows 
            #print("Total no. of rows: %d"%(csvreader.line_num)) 
          
        # #printing the field names 
        #print('Field names are:' + ', '.join(field for field in fields)) 
        #print(fields)
        #print(rows)

        for row in rows: 
            # parsing each column of a row 
            #print(row)
            if row[2]==str(self.testc_arg):
                for col in row: 
                    #print("columns",col)
                    data[fields[counter]]=col
                    counter+=1
            if counter>0:
                break
            
        return data

    def Get_Parameters_By_Sheet(self,testc_arg,test_sheet_arg):
        self.param_arg = {} 
        filename = test_sheet_arg
        self.testc_arg = testc_arg  
        # initializing the titles and rows list 
        fields = [] 
        rows = [] 

        counter = 0
        
        #print(filename)
        
        # reading csv file 
        with open(filename, 'r') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
              
            # extracting field names through first row 
            fields = next(csvreader) 

            ##print(csvreader)
            # extracting each data row one by one 
            for row in csvreader:
                print(row) 
                if not len(row)==0:
                    rows.append(row) 
          
            # get total number of rows 
            ##print("Total no. of rows: %d"%(csvreader.line_num)) 
          
        # #printing the field names 
        print('Field names are:' + ', '.join(field for field in fields)) 
        ##print(fields)
        print(rows)
        flag = 0
        for row in rows: 
            # parsing each column of a row 
            print(row)
            if row[1]==str(self.testc_arg):
                if not len(row)==0:
                    try:
                        Param = str(row[4]).split("::")
                        for plg in Param:
                            flag+= 1
                            Plugin_Param = str(plg).split("--")
                            self.param_arg[Plugin_Param[0]]=Plugin_Param[1]
                        
                        if flag>0:
                            return self.param_arg
                    except:
                        break
                        return False
                            
        #return self.param_arg
    
#===============================================================================
class GetRoot_Path():
    def Get_root(self):
        return self.Path(__file__).parent.parent
        #=======================================================================
        # dir1 = os.path.realpath('.')
        # #print(dir1.split("test_py_proj"))
        # root_path = dir1.split("test_py_proj")[0]
        #=======================================================================
        #return root_path
#===============================================================================
#===============================================================================
 