import pytest
from selenium import webdriver
import undetected_chromedriver as uc

@pytest.fixture(scope="class")
def setup(request,browser):
    if browser == 'uc':
        driver=uc.Chrome()
        
        print("Opening undetected webdriver")
    if browser=='chrome':
        options=webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver=webdriver.Chrome(options=options)
        
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    request.cls.driver = driver
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

# @pytest.fixture()
@pytest.fixture(scope="class")
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    # config._metadata['Project Name'] = 'nop Commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Pavan'
    pass

# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
