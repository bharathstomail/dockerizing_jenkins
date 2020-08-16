from selenium import webdriver
from selenium.webdriver import ChromeOptions
import pytest
import logging
import allure
import json
from pathlib import Path

driver = None
 
#===============================================================================
# @pytest.fixture(scope='class', autouse=True)
# def driver_url(request):
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#         request.cls.driver = driver
#         driver.maximize_window()
#     yield
#     driver.close()
#     driver.quit()
#     Send_Reports()
#===============================================================================

#===============================================================================
# @pytest.fixture(scope='module',autouse=True)
# def driver_url(request):
#     global driver
#     if driver is None:
#         #options = ChromeOptions()
#         #options.add_argument('--disable-dev-shm-usage')
#         #options.add_argument('headless')
#         #options.add_argument('no-sandbox')
#         #options.add_argument('window-size=1200x800')
#         #desired_caps = options.to_capabilities()
#         #desired_caps['platform'] = 'Linux'
#         
#         options = ChromeOptions()
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--ignore-certificate-errors')
#         desired_caps = options.to_capabilities()
#         
#         data = get_system_details()
#             
#         print(data['Remote_Node_IP'])
#         print(data['Remote_Node_Port'])
#         print('http://'+data['Remote_Node_IP']+':'+data['Remote_Node_IP']+'/wd/hub')
#         
#         driver = webdriver.Remote(command_executor='http://'+data['Remote_Node_IP']+':'+data['Remote_Node_Port']+'/wd/hub',desired_capabilities=desired_caps)        
#         
#         #driver = webdriver.Remote(command_executor='http://161.85.25.246:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
# 
#         request.cls.driver = driver
#         driver.maximize_window()
#     return driver
#===============================================================================

def get_system_details():
    project_Packg_Path = str(Path(__file__).parent.parent.parent)
    path_arg = project_Packg_Path+'\\Test_Resources\\Config.json'
    with open(path_arg) as o1:
        data = json.loads(o1.read())
    return data  

#@pytest.fixture(scope='class', autouse=True)
def report_step(step_title):
    with allure.step(step_title):
        pass

#def pytest_configure(config):
#    allure.environment(report='ISD Test Automation report', browser=u'Chrome')

#@pytest.fixture(scope="class")
#def app_host_name():
#    host_name = "my.host.local"
#    allure.environment(hostname=host_name)
#    return host_name

#@pytest.mark.parametrize('country', ('USA', 'Germany'))
#def test_minor(country):
#    allure.environment(country=country)
#    assert country


class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('Log {}'.format(message)):
            pass

    def emit(self, record):
        self.log("({}) {}".format(record.levelname, record.getMessage()))

class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()
    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)
    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield
