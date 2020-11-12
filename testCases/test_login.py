import pytest,logging
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    
    logs = LogGen.loggen()
    logs.info('sssddd')
    print(logs)

    def test_log(self):
        self.logs.info('***** Test_001_Login *****')

    '''
    def test_homePageTitle(self,setup):
        self.logger.info("***** Test_001_Login *****")
        self.logger.info("***** Verifying Home Page title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("***** Home Page title test is passed *****")
            self.driver.close()
        else :
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("***** Home Page title test is failed *****")
            self.driver.close()
            assert False
    
    def test_login(self,setup):
        self.logger.info("***** Test_001_Login *****")
        self.logger.info("***** Verifying Login test *****")
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
            self.logger.info("***** Login test is passed *****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
            self.logger.error("***** Login test is failed *****")
    '''