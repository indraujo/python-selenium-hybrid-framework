import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logs = LogGen.loggen()
    '''
    def test_log(self):
        logs = LogGen.loggen()
        print(self.logs)
        self.logs.info("***** Test_001_Login *****")

    
    def test_homePageTitle(self,setup):
        self.logs.info("***** Test_002_DDT_Login *****")
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
    '''
    def test_login(self,setup):
        self.logs.info("***** Test_002_Login *****")
        self.logs.info("***** Verifying Login DDT test *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)
        lst_status = []

        for r in range(2,self.rows+1):
            #self.logs.info("***** Test Row "+ str(r) +" *****")

            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.passw = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)
            print(self.user)
            print("test",str(r))
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.passw)
            self.lp.clickLogin()
            time.sleep(5)
            
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logs.info("***** Test Pass *****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logs.info("***** Test Fail *****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logs.info("***** Test Fail *****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logs.info("***** Test Pass *****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logs.info("***** Login DDT Test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logs.info("***** Login DDT Test Failed *****")
            assert False

        self.logs.info("***** End Of Login DDT Test Passed *****")
        self.logs.info("***** Complete Of Login DDT Test Passed *****")
