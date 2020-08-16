

#@author: Bharath HS

from Package_ISD.ISD_Library_Files.Read_Data_Setup import Read_Excel,GetRoot_Path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import traceback
import sys
import allure
import logging
from allure_commons.types import AttachmentType
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from Package_ISD.ISD_Library_Files.Report_HTML import Report_HTML

class Element_Activities():
    #===========================================================================
    # def __init__(self, col_name_arg):
    #===========================================================================

    def __init__(self,driver_arg):
        #=======================================================================
        # self.test_case_arg = test_case_arg
        #self.sheet_arg = sheet_arg
        #self.col_name_arg = col_name_arg
        #self.Report_Path = Report_Path
        self.driver_arg = driver_arg
        #self.Report_Instance = Report_Instance
        #=======================================================================
        self.dict_arg = {}

    def report_step(self,step_title):
        with allure.step(step_title):
            pass

    def logger_util(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
   
    #===========================================================================
    # #===========================================================================
    # def public(self):
    #     self.Report_Instance = Report_HTML(self.Report_Path,self.driver)
    # #===========================================================================
    #===========================================================================
     
    def encrypt(self,message):
        newS=''
        for car in message:
            newS=newS+chr(ord(car)+2)
        
        return str(newS)
        
    def get_field_Input(self,test_case_arg):
        self.test_case_arg = test_case_arg 
        class_details = Read_Excel(self.sheet_arg,self.col_name_arg)
        rootnode = GetRoot_Path()
        var2 = rootnode.Get_root()
        class_details.Get_Excelconn(var2+"/Test_Resources/Data_Setup.xls")
        self.dict_arg = class_details.Get_ExcelData(self.test_case_arg)
        
        for key_val2 in self.dict_arg.keys():
            print(self.dict_arg.__getitem__(key_val2))
        
        return self.dict_arg
    
    def Get_Config_Details(self,test_case_arg):
        self.test_case_arg = test_case_arg
        
        config_info = Read_Excel()
        rootnode = GetRoot_Path()
        var2 = rootnode.Get_root()
        config_info.Get_Excelconn(var2+"/Test_Resources/Data_Setup.xls")
        self.dict_arg = config_info.Get_ExcelData()
        
        for key_val3 in self.dict_arg.keys():
            print(self.dict_arg.__getitem__(key_val3))
        
        return self.dict_arg
    
    def Perform_Element_Activities(self,driver_object,attname_arg,attval_arg):
        self.driver_object = driver_object
        self.obj_Attrname = attname_arg
        self.obj_AttrVal = attval_arg

        #=======================================================================
        # self.keyword_obj = self.get_field_Input(test_case_arg)
        #=======================================================================
        
        print(self.driver_object.title)
        if(self.obj_Attrname=="id"):
            Web_Element = WebDriverWait(self.driver_object,15).until(expected_conditions.visibility_of_element_located((By.ID,self.obj_AttrVal)))
            #===================================================================
            # Web_Element = self.driver_object.find_element_by_id(self.obj_AttrVal)
            #===================================================================

        elif(self.obj_Attrname=="xpath"):
            Web_Element = WebDriverWait(self.driver_object,15).until(expected_conditions.visibility_of_element_located((By.XPATH,self.obj_AttrVal)))
            #===================================================================
            # Web_Element = self.driver_object.find_element_by_xpath(self.obj_AttrVal)
            #===================================================================

        elif(self.obj_Attrname=="partial_link_text"):
            Web_Element = WebDriverWait(self.driver_object,15).until(expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT,self.obj_AttrVal)))
            #===================================================================
            # Web_Element = self.driver_object.find_element_by_partial_link_text(self.obj_AttrVal)
            #===================================================================

        elif(self.obj_Attrname=="link_text"):
            Web_Element = WebDriverWait(self.driver_object,15).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,self.obj_AttrVal)))
                #===============================================================
                # Web_Element = self.driver_object.find_element_by_link_text(self.obj_AttrVal)
                #===============================================================

        elif(self.obj_Attrname=="name"):
            Web_Element = WebDriverWait(self.driver_object,15).until(expected_conditions.visibility_of_element_located((By.NAME,self.obj_AttrVal)))
            #===================================================================
            # Web_Element = self.driver_object.find_element_by_name(self.obj_AttrVal)
            #===================================================================

        elif(self.obj_Attrname=="css_selector"):
            Web_Element = WebDriverWait(self.driver_object,15).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,self.obj_AttrVal)))
            #===================================================================
            # Web_Element = self.driver_object.find_element_by_css_selector(self.obj_AttrVal)
            #===================================================================
   
        return Web_Element
  
    def Verify_Element_Validate(self,driver_object,element_arg,ele_ident_type):
        self.driver_object = driver_object
        #self.element_arg = element_arg
        #self.ele_ident_type = ele_ident_type
        #self.keyword_obj = self.get_field_Input(test_case_arg)
        #self.log_arg = log_arg

        #Creating the report instance to enter the logs at testcasename.html file
        #self.Report_Inst = self.Report_HTML(self.Report_filepath,self.driver_object)
        
        self.Att_name = ele_ident_type
        self.Att_val = element_arg
        #self.Att_Object = self.keyword_obj.__getitem__("Object")
        
        #print(self.Att_name+","+self.Att_val+","+self.Att_Object)
        self.Ele_obj = self.Perform_Element_Activities(self.driver_object,self.Att_name,self.Att_val)
          
        if self.Ele_obj.is_displayed():
            print("True")
            return self.Ele_obj
        else:
            print("No Element Exists")
                
                
                
    def Webelement_Editbox(self,driver_object,element_obj,element_input_arg,element_objtype,field_arg):
        try:
            self.driver_object = driver_object
            self.element_obj = element_obj
            self.element_objtype = element_objtype    
            self.element_input_arg = element_input_arg
            self.field_arg = field_arg
            #self.Report_Instance = Report_HTML(self.Report_Path,self.Get_Driver)
            if(self.element_objtype=="editbox"):
                if(self.element_obj.is_enabled()):
                    self.element_obj.clear()
                    self.driver_object.implicitly_wait(30)
                    
                    print(self.element_input_arg)
                    self.element_obj.send_keys(self.element_input_arg)
                    
                    if(self.field_arg=="Password"):
                        element_input_arg = self.encrypt(element_input_arg)
                        self.report_step("User is able to enter the details : "+str(element_input_arg))
                        allure.attach(self.driver_object.get_screenshot_as_png(), name=str(self.field_arg), attachment_type=AttachmentType.PNG)
                        self.driver_object.implicitly_wait(30)
                else:
                    #LogUtil.log("User is Unable to enter the details : "+str(element_input_arg));
                    self.report_step("User is Unable to enter the details : "+str(element_input_arg))
                    allure.attach(self.driver_object.get_screenshot_as_png(), name=str(self.field_arg), attachment_type=AttachmentType.PNG)
        except:
            print(traceback.format_exc())
            print(sys.exc_info()[0])
            #self.report_step("Encountered with an Exception : "+str(traceback.format_exc() + "--- "+ str(sys.exc_info()[0])))
            #self.LogUtil.log("Encountered with an Exception : "+str(traceback.format_exc() + "--- "+ str(sys.exc_info()[0])));
            allure.attach(self.driver_object.get_screenshot_as_png(), name="Encountered with an Exception", attachment_type=AttachmentType.PNG)
            #self.Report_Instance.Report_Log(self.field_arg,"User should be able to enter the details","Encountered with an exception - "+str(traceback.format_exc() + "--- "+ str(sys.exc_info()[0])),"")

    def Webelement_element(self,driver_object,element_objname,element_objVal,element_objtype):
        try:
            self.driver_object = driver_object
            #self.element_obj = element_obj
            self.element_objname = element_objname
            self.element_objVal = element_objVal
            self.element_objtype = element_objtype
            #self.field_arg = field_arg   
            
            if(self.element_objtype=="element"):
                if(self.element_objname =="id"):
                    self.click_ele = WebDriverWait(self.driver_object,10).until(expected_conditions.element_to_be_clickable((By.ID,self.element_objVal)))
                    #self.click_ele.click()                                                                                 
                    self.driver_object.implicitly_wait(30)
                    return self.click_ele
                    
                elif(self.element_objname =="xpath"):
                    self.click_ele = WebDriverWait(self.driver_object,10).until(expected_conditions.element_to_be_clickable((By.XPATH,self.element_objVal)))
                    self.driver_object.implicitly_wait(30)
                    return self.click_ele
                    
                elif(self.element_objname =="partial_link_text"):
                    self.click_ele = WebDriverWait(self.driver_object,10).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT,self.element_objVal)))
                    #self.click_ele.click()                                                                                 
                    self.driver_object.implicitly_wait(30)
                    return self.click_ele
                    
                elif(self.element_objname =="link_text"):
                    self.click_ele = WebDriverWait(self.driver_object,10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,self.element_objVal)))
                    #self.click_ele.click()                                                                                 
                    self.driver_object.implicitly_wait(30)
                    return self.click_ele
                    
                elif(self.element_objname =="class_name"):
                    self.click_ele = WebDriverWait(self.driver_object,10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,self.element_objVal)))
                    #self.click_ele.click()                                                                                 
                    self.driver_object.implicitly_wait(30)
                    return self.click_ele
        except:
            print(driver_object.description)
            
            
    def Force_Logout(self):
        print("logout")
        
    def Webelement_Link(self,driver_object,element_objname,element_objVal,element_objtype):
        self.driver_object = driver_object
        #self.element_obj = element_obj
        self.element_objname = element_objname
        self.element_objVal = element_objVal
        self.element_objtype = element_objtype   
        
        if(self.element_objtype=="Link" or "partial_link_text" or "link_text"):
            if(self.element_objname =="id"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.ID,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="xpath"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.XPATH,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="partial_link_text"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="link_text"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="class_name"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)
                
    def WebElement_Button(self,driver_object,element_objname,element_objVal,element_objtype):
        self.driver_object = driver_object
        #self.element_obj = element_obj
        self.element_objname = element_objname
        self.element_objVal = element_objVal
        self.element_objtype = element_objtype
        
        if(self.element_objtype=="button"):
            if(self.element_objname =="id"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.ID,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="xpath"):
                print("entered xpath - "+self.element_objVal)
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.XPATH,self.element_objVal)))
                self.click_ele.click()                                                                               
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="partial_link_text"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT,self.element_objVal)))
                self.click_ele.click()                                                                                
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="link_text"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)
            elif(self.element_objname =="class_name"):
                self.click_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,self.element_objVal)))
                self.click_ele.click()                                                                                 
                self.driver_object.implicitly_wait(30)                 
        
    def WebElement_Check_Radio(self,driver_object,element_obj,element_objname,element_objVal,element_objtype,element_input_arg):
        self.driver_object = driver_object
        self.element_obj = element_obj
        self.element_objname = element_objname
        self.element_objVal = element_objVal
        self.element_objtype = element_objtype
        self.element_input_arg = element_input_arg
                
        if(self.element_objtype=="Check_Box"):
            if(self.element_objname =="xpath"):
                self.click_ele =  WebDriverWait(self.driver_object,2).until(expected_conditions.element_located_selection_state_to_be((By.XPATH,self.element_objVal)))
                if not(self.click_ele==self.element_input_arg):
                    self.click_ele.click()
            elif(self.element_objname =="id"):
                self.click_ele =  WebDriverWait(self.driver_object,2).until(expected_conditions.element_located_selection_state_to_be((By.ID,self.element_objVal)))
                if not(self.click_ele==self.element_input_arg):
                    self.click_ele.click()
            elif(self.element_objname =="class_name"):
                self.click_ele =  WebDriverWait(self.driver_object,2).until(expected_conditions.element_located_selection_state_to_be((By.CLASS_NAME,self.element_objVal)))
                if not(self.click_ele==self.element_input_arg):
                    self.click_ele.click()

        if(self.element_objtype=="Radio_Button"):
            if(self.element_objname =="xpath"):
                self.click_ele =  WebDriverWait(self.driver_object,2).until(expected_conditions.element_located_selection_state_to_be((By.XPATH,self.element_objVal)))
                if not(self.click_ele==self.element_input_arg):
                    self.click_ele.click()
            elif(self.element_objname =="id"):
                self.click_ele =  WebDriverWait(self.driver_object,2).until(expected_conditions.element_located_selection_state_to_be((By.ID,self.element_objVal)))
                if not(self.click_ele==self.element_input_arg):
                    self.click_ele.click()
            elif(self.element_objname =="class_name"):
                self.click_ele =  WebDriverWait(self.driver_object,2).until(expected_conditions.element_located_selection_state_to_be((By.CLASS_NAME,self.element_objVal)))
                if not(self.click_ele==self.element_input_arg):
                    self.click_ele.click()

    def Switch_Frame(self,driver_object,element_objtype,element_objname,element_objVal):
        self.driver_object = driver_object
        self.element_objname = element_objname
        self.element_objtype = element_objtype
        self.element_objVal = element_objVal
        
        if(self.element_objtype=="frame"):
            if(self.element_objname == "id"):
                print(self.element_objVal)
                try:
                    element_present = expected_conditions.presence_of_element_located((By.ID,self.element_objVal))
                    WebDriverWait(self.driver_object,20).until(element_present)
                except:
                        print("Timed out waiting for page to load")
                finally:
                        print("To Determine the element available on page load in 20 secs")
        
   
                self.driver_object.switch_to_frame(self.driver_object.find_element_by_id(self.element_objVal))
                          
            elif(self.element_objname == "name"):
                
                try:
                    element_present = expected_conditions.presence_of_element_located((By.NAME,self.element_objVal))
                    WebDriverWait(self.driver_object,20).until(element_present)
                except:
                        print("Timed out waiting for page to load")
                finally:
                        print("To Determine the element available on page load in 20 secs")
                        
                self.driver_object.switch_to_frame(self.driver_object.find_element_by_name(self.element_objVal))
            
            elif(self.element_objname == "tag"):
                print("entered tag")
                try:
                    element_present = expected_conditions.presence_of_element_located((By.TAG_NAME,self.element_objVal))
                    WebDriverWait(self.driver_object,20).until(element_present)
                except:
                        print("Timed out waiting for page to load")
                finally:
                        print("To Determine the element available on page load in 20 secs")
                        
                #self.frame_ele = WebDriverWait(self.driver_object,2).until(expected_conditions.frame_to_be_available_and_switch_to_it(self.element_objVal))
                #self.frame_ele.switch_to_frame(element_objVal)
                self.driver_object.switch_to_frame(self.driver_object.find_element_by_tag_name(self.element_objVal))

