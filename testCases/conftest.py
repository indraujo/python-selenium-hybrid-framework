from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome("C:\\Users\\LENOVO\\Documents\\GitHub\\python-selenium-hybrid-framework\\chromedriver.exe")
    return driver