from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome("C:\\Users\\LENOVO\\Documents\\GitHub\\python-selenium-hybrid-framework\\chromedriver.exe")
        print("----- Launching Chrome -----")
    elif browser=="firefox":
        driver = webdriver.Firefox()
        print("----- Launching Firefox -----")
    else:
        driver = webdriver.Ie()    
        print("----- Launching Edge -----")
    return driver

def pytest_addoption(parser): # this will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the browser vluer to setup method
    return request.config.getoption("--browser")

#-------------- PyTest HTML Report ------------------#
# it;s hook foradding Enviroment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# it's hook for delete/modify enviroment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)