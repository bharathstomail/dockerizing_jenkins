

from Package_ISD.ISD_Library_Files.Read_Data_Setup import Read_Excel
from Package_ISD.ISD_Library_Files.Common_Functions import Common_Class
from Package_ISD.ISD_Library_Files.Application_Functions import Application_Function
from Package_ISD.ISD_Library_Files.Image_Processing_Module import Image_Processing
from selenium.webdriver.common.keys import Keys
import time
import sys

#Factory method to create the instance of the class
def get_obj(obj=''):
    objs = dict(Excep_Operation=Read_Excel(),Common_Class_Functions = Common_Class(),Application_Modules = Application_Function(),Image_Processing_Activities = Image_Processing())
    return objs[obj]

#Below method will read the data from excel with reference to the Test case ID
def data_preparation(dict_obj,test_arg,root_path):
    try:
        Excep_Operation = get_obj('Excep_Operation')
        sheet_name = Excep_Operation.csv_from_excel(root_path+"/Test_Resources/")
        #Excep_Operation.Get_Excelconn(root_path+"/Test_Resources/Data_Setup.xls")
        dict_obj = Excep_Operation.Get_ExcelData(sheet_name['Test_Data'],test_arg)
        return dict_obj,sheet_name
    except:
        raise AssertionError(str(sys.exc_info()[0]))


def switch_windows(driver_arg):
    driver_arg.switch_to_default_content()
    window_list = driver_arg.window_handles
    print(len(window_list))
    driver_arg.switch_to_window(window_list[1])
    print("title ------>:"+driver_arg.title)
    return driver_arg.title

# Check the data availability & Launch the respective application
def check_data_launch_App(driver,CClass_func,App_Modules,ele_activities,TD):
    Locator_List = CClass_func.Read_Locators('PD_Frame')
    print(Locator_List)
    ele_activities.Switch_Frame(driver,Locator_List[2],Locator_List[1],Locator_List[3])
    driver.implicitly_wait(30)
    
    Locator_List = CClass_func.Read_Locators('PD_List')
    Search_field = CClass_func.Read_Locators("Search_field")
    Search_field_1 = CClass_func.Read_Locators("Search_field_1") 
    
    if driver.find_element_by_xpath(Search_field[3]).is_displayed():
        PD_Data = str(TD.__getitem__("Patient_Data"))
        print(PD_Data)
        searchfield = driver.find_element_by_xpath(Search_field[3])
        
        driver.execute_script("arguments[0].value = arguments[1]", searchfield, str(PD_Data))
        time.sleep(1)
        try:
            driver.find_element_by_xpath(Search_field[3]).send_keys(" ")
            time.sleep(1)
            driver.find_element_by_xpath(Search_field_1[3]).send_keys(u'\ue003')
            time.sleep(1)
            driver.find_element_by_xpath(Search_field_1[3]).send_keys(Keys.RETURN)
            print("tried RETURN")
        except:
            driver.find_element_by_xpath(Search_field_1[3]).send_keys(Keys.ENTER)
            print("tried ENTER")
    time.sleep(1)
    table_patients = driver.find_elements_by_xpath(Locator_List[3])
    
    print(len(table_patients))
    
    if len(table_patients)==0:
        App_Modules.Upload_Patient_Data(TD.__getitem__("Patient_Data_Upload"),driver)
        time.sleep(2)
        App_Modules.Launch_Patient_Data(driver,TD)
        time.sleep(1)
    elif len(table_patients)>0:
        time.sleep(1) 
        App_Modules.Launch_Patient_Data(driver,TD)
