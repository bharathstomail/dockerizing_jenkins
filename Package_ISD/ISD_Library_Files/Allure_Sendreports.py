import os, requests, json, base64
from pathlib import Path

def Read_Json_File():
    #self.param_arg = param_arg
    project_Packg_Path = str(Path(__file__).parent.parent)
    path_arg = project_Packg_Path+'/Test_Resources/Config.json'
    with open(path_arg) as o1:
        data = json.loads(o1.read())
    return data

def Send_Reports():
    project_Packg_Path = str(Path(__file__).parent.parent)
    # This directory is where you have all your results locally, generally named as `allure-results`
    allureResultsDirectory = project_Packg_Path+'/Test_Report/allure_docker_dir'
    #allureResultsDirectory = 'E:/SeleniumBaseImage/Approach_2/Allure_docker/allure-results/'
    
    # This url is where the Allure container is deployed. We are using localhost as example
    config_data = Read_Json_File()
    
    #allureServer = 'http://161.85.25.246:5050'
    allureServer = config_data['allureServer']
    
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    print(currentDirectory)
    resultsDirectory = allureResultsDirectory
    print('RESULTS DIRECTORY PATH: ' + resultsDirectory)
    
    files = os.listdir(resultsDirectory)
    
    print('FILES:')
    results = []
    for file in files:
        result = {}
    
        filePath = resultsDirectory + "/" + file
        print(filePath)
    
        if os.path.isfile(filePath):
            try:
                with open(filePath, "rb") as f:
                    content = f.read()
                    if content.strip():
                        b64Content = base64.b64encode(content)
                        result['file_name'] = file
                        result['content_base64'] = b64Content.decode('UTF-8')
                        results.append(result)
                    else:
                        print('Empty File skipped: '+ filePath)
            finally :
                f.close()
        else:
            print('Directory skipped: '+ filePath)
    
    headers = {'Content-type': 'application/json'}
    requestBody = {
        "results": results
    }
    #print(requestBody)
    jsonRequestBody = json.dumps(requestBody)
    
    response = requests.post(allureServer + '/send-results', headers=headers, data=jsonRequestBody)
    print("RESPONSE:",response)
    jsonResponseBody = json.loads(response.content)
    jsonPrettierResponseBody = json.dumps(jsonResponseBody, indent=4, sort_keys=True)
    print(jsonPrettierResponseBody)
    print("STATUS CODE:")
    print(response.status_code)
    
Send_Reports()