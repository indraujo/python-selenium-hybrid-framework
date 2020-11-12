import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    
    logs = LogGen.loggen()
    
    def test_log(self):
        logs = LogGen.loggen()
        print(self.logs)
        self.logs.info("***** Test_001_Login *****")

    
    def test_homePageTitle(self,setup):
        self.logs.info("***** Test_001_Login *****")
        self.logs.info("***** Verifying Home Page title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logs.info("***** Home Page title test is passed *****")
            self.driver.close()
        else :
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logs.error("***** Home Page title test is failed *****")
            self.driver.close()
            assert False
    
    def test_login(self,setup):
        self.logs.info("***** Test_001_Login *****")
        self.logs.info("***** Verifying Login test *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.lp.clickLogout()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logs.info("***** Login test is passed *****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
            self.logs.error("***** Login test is failed *****")
    