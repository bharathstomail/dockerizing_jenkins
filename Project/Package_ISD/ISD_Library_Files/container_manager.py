
import requests
import json
import os
from pathlib import Path

def Read_Json_File():
    #self.param_arg = param_arg
    try:
        pckg_path = str(os.getcwd()).split("/")
        Get_Path = '/'.join(map(str,pckg_path[0:int(pckg_path.index("Package_ISD"))+1]))
        print(Get_Path)
    except:
        Get_Path = str(Path(__file__).parent.parent)
        
    print(Get_Path)
    path_arg = Get_Path+'/Test_Resources/Config.json'
    with open(path_arg) as o1:
        data = json.loads(o1.read())
    return data

class Container_manager():
    
    __slots__ = ["url_arg_1","url_arg_2","config","response","response_data","port_id"]
    
    def __init__(self):
        self.config = Read_Json_File()
        self.url_arg_1 = self.config.__getitem__("container_req")
        self.url_arg_2 = self.config["delete_container"]


    def container_request(self):
        try:
            self.url_arg_1 = self.config.__getitem__("container_req")
            headers = {'Content-type': 'application/json'}
            self.response = requests.get(self.url_arg_1,headers=headers)
            print("response",self.response.status_code)
            self.response_data = self.response.json()
            print(self.response_data)
            assert self.response.status_code==200,"Failed to get the container id. Response status code is - " + self.response.status_code
            return self.response_data
        except Exception as e:
            print("Exception error {}".format_map(e))
    
    def delete_container(self,port_arg):
        try:
            self.port_id = port_arg
            header = {'Content-type': 'application/json'}
            self.response = requests.post(self.url_arg_2+str(self.port_id),headers=header)
            print("response",self.response.status_code)
            self.response_data = self.response.json()
            print(self.response_data)
            assert self.response.status_code==200,"Failed to post the container id. Response status code is - " + self.response.status_code   
            return self.response_data
        except Exception as e:
            print("Exception error {}".format_map(e))


cont_mgr = Container_manager()
cr = cont_mgr.container_request()
print(cr)

print(cont_mgr.delete_container(cr))