
#@author: Bharath HS

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver import ChromeOptions
from Package_ISD.ISD_Library_Files.Allure_Sendreports import Send_Reports
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os
import datetime
import json
import socket
from pathlib import Path
from Package_ISD.ISD_Library_Files.Read_Data_Setup import Read_Excel,GetRoot_Path
from selenium.webdriver.common.action_chains import ActionChains
import allure
from Package_ISD.ISD_Library_Files.container_manager import Container_manager
#from Package_ISD.ISD_Library_Files.Report_HTML import Report_HTML

class Common_Class():
    def __init__(self):
        pckg_path = str(os.getcwd()).split("/")
        self.project_Packg_Path = '/'.join(map(str,pckg_path[0:int(pckg_path.index("Package_ISD"))+1]))
        #self.project_Packg_Path = str(Path(__file__).parent.parent)
        self.cont_mgr = Container_manager()
      
    def Read_Json_File(self):
        #self.param_arg = param_arg
        pckg_path = str(os.getcwd()).split("/")
        self.Get_Path = '/'.join(map(str,pckg_path[0:int(pckg_path.index("Package_ISD"))+1]))
        print(self.Get_Path)
        #self.project_Packg_Path = str(Path(__file__).parent.parent)
        path_arg = self.Get_Path+'/Test_Resources/Config.json'
        with open(path_arg) as o1:
            data = json.loads(o1.read())
        return data

    #-------------Template ---------------------------------------
    #updateJsonFile("Plugin_Liver_Segmentation","PASSED")
    def updateJsonFile(self,Test_Case_Arg,Test_Case_status):
        with open(self.project_Packg_Path+'/Test_Resources/Config.json', "r") as jsonFile:
            data = json.load(jsonFile)
        
        #tmp = data["location"]
        data[Test_Case_Arg] = Test_Case_status
        
        with open(self.project_Packg_Path+'/Test_Resources/Config.json', "w") as jsonFile:
            json.dump(data, jsonFile)
      
    def Report_dir(self,file_path):
        self.file_path = file_path
        #directory = os.path.dirname(file_path)
        #print(directory)
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
            self.r_path = self.file_path + "Run_1/"
            os.makedirs(self.r_path)
            return self.r_path
        elif os.path.exists(self.file_path):
            dir_count = 0
            for root, dirs, files in os.walk(self.file_path):
                for name in dirs:
                    #print(name)
                    dir_count+=1
            
            if dir_count>0:
                dir_count+=1
                self.r_path = str(self.file_path+"Run_"+str(dir_count)+"/")
                os.makedirs(self.r_path)
                return self.r_path
            elif dir_count<1:
                dir_count+=1
                self.r_path = str(self.file_path+"Run_"+str(dir_count)+"/")
                os.makedirs(self.r_path)
                return self.r_path
    
    def get_project_root(self):
    #"""Returns project root folder."""
        return str(Path(__file__).parent.parent)

    #def Get_Driver(self,extension_arg):
    def Get_Driver(self):        
        #self.project_Packg_Path = self.get_project_root()
        
        #Below code to bypass the bootstrap login to server
        #EXTENSION_ROOT = os.path.join(self.project_Packg_Path+'/',extension_arg)
        #print(EXTENSION_ROOT)
        
        options = webdriver.ChromeOptions()
        #options.add_argument('load-extension={0}'.format(EXTENSION_ROOT))
        
        
        driver = webdriver.Chrome(chrome_options=options)
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        
        driver.maximize_window()
        return driver 
    
    def Get_Remote_driver(self):
        local_ip = socket.gethostbyname(socket.gethostname())
        print(local_ip)
        
        # Below code for Remote selenium standalone server vm details
        #driver = webdriver.Remote(command_executor='http://161.85.25.12:5556/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
        
        data = self.Read_Json_File()
        options = ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        desired_caps = options.to_capabilities()

        self.port_id = self.cont_mgr.container_request()
        time.sleep(5)
        
        # Below code for Remote selenium standalone server docker container details
        driver = webdriver.Remote(command_executor='http://'+data['Remote_Node_IP']+':'+self.port_id+'/wd/hub',desired_capabilities=desired_caps)
        
        #driver = webdriver.Remote(command_executor='http://localhost:'+port_id+'/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
        #driver.get("http://161.85.25.77/isdiscovery")
        driver.maximize_window()
        return driver

    def end_script(self,driver_arg):
        self.driver = driver_arg 
               
        self.driver.close()
        self.driver.quit()
        Send_Reports()

    #===========================================================================
    # def driver(self,dict_obj):
    #     self.dict = dict_obj
    #     print(self.dict)
    #     if self.dict.__getitem__("Remote_Execution") is not None:
    #         port_id = self.dict.__getitem__("Port_ID")
    #         driver_arg = self.Get_Remote_driver(port_id)
    #         
    #     elif self.dict.__getitem__("Remote_Execution") is None:
    #         driver_arg = self.Get_Driver()
    #     
    #     return driver_arg
    #===========================================================================
    
    def Read_Locators(self,locator_ref):
        file = open(self.project_Packg_Path+"/Locator_File/Locator.txt",'r') 
        for line in file:
            #print(line)
            if str(line).startswith(locator_ref):
                line_item = str(line).strip()
                get_xpath = str(line_item).split(" -- ")
                break
        #return get_xpath[1]
        return get_xpath
    
    #definition for segmentation - approach1
    def Segmentation_3D_ROI(self,driver_arg,element_arg,x_offset,mode):
        size = element_arg.size
        wd = size['width']
        ht = size['height']
        
        wd_x = float(wd/2)
        X = int(round(wd_x))
        
        ht_y = float(ht/2)
        Y = int(round(ht_y))
        
        if mode=="Addition":
            X = X+int(x_offset)
        elif mode=="Subtraction":
            X = X-int(x_offset)
        
        try:
            ActionChains(driver_arg).move_to_element_with_offset(element_arg,X,Y).click().perform()
            time.sleep(2)
            #ActionChains(driver).move_to_element(element).click().perform()
            ActionChains(driver_arg).move_to_element_with_offset(element_arg,X,Y).click_and_hold().perform()
            ActionChains(driver_arg).move_by_offset(X/10,Y/10).perform()
            time.sleep(3)
            ActionChains(driver_arg).release().perform().build()
        except:
            time.sleep(1)
            pass
        
        print("mouse pointer is dragged and dropped")
        time.sleep(5)

    #definition for segmentation - approach2
    def Segmentation_3D_ROI_1(self,driver_arg,element_arg,x_offset,mode):
        size = element_arg.size
        wd = size['width']
        ht = size['height']
        
        wd_x = float(wd/2)
        X = int(round(wd_x))
        
        ht_y = float(ht/2)
        Y = int(round(ht_y))
        
        if mode=="Addition":
            X = X+int(x_offset)
        elif mode=="Subtraction":
            X = X-int(x_offset)
        
        try:
            ActionChains(driver_arg).move_to_element_with_offset(element_arg,X,Y).click().perform()
            time.sleep(2)
            #ActionChains(driver).move_to_element(element).click().perform()
            ActionChains(driver_arg).drag_and_drop_by_offset(element_arg,X/10,Y/10).perform().build()
            #ActionChains(driver_arg).dragAndDropBy(element_arg,X/10,Y/10)
            #ActionChains(driver_arg).move_to_element_with_offset(element_arg,X,Y).click_and_hold().perform()
            #ActionChains(driver_arg).move_by_offset(X/10,Y/10).perform()
            time.sleep(3)
            #ActionChains(driver_arg).release().perform().build()
        except:
            time.sleep(1)
            pass
        
        print("mouse pointer is dragged and dropped")
        time.sleep(5)

#below class is to get the single instance of the report path

class Report_Directory_Instance():
    
    _instance = None
    
    def __init__(self,file_path):
        self.r_path = file_path
        self.report_path = self.Report_dir(self.r_path)
          
    def Report_dir(self,file_path):
        self.file_path = file_path
        #directory = os.path.dirname(file_path)
        #print(directory)
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
            self.r_path = self.file_path + "Run_1/"
            os.makedirs(self.r_path)
            return self.r_path
        elif os.path.exists(self.file_path):
            dir_count = 0
            for root, dirs, files in os.walk(self.file_path):
                for name in dirs:
                    #print(name)
                    dir_count+=1
            
            if dir_count>0:
                dir_count+=1
                self.r_path = str(self.file_path+"Run_"+str(dir_count)+"/")
                os.makedirs(self.r_path)
                return self.r_path
            elif dir_count<1:
                dir_count+=1
                self.r_path = str(self.file_path+"Run_"+str(dir_count)+"/")
                os.makedirs(self.r_path)
                return self.r_path
            
class Get_Report_Instance():

    @staticmethod 
    def Return_Report_Instance():
        Get_Path = str(Path(__file__).parent.parent)
        now = datetime.datetime.now()
        time_stamp = str(now.strftime('%Y-%m-%d'))
        Time_stamp_folder = time_stamp.replace(":","_").replace("-","_").replace(" ","_")
        Report_Path = Get_Path+"/Test_Report/"+Time_stamp_folder+"/"
        
        if Report_Directory_Instance._instance is None:
            Report_Directory_Instance._instance = Report_Directory_Instance(Report_Path)
        return Report_Directory_Instance._instance
