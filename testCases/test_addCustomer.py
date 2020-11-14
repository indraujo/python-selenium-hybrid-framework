import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_003_AddCustomer:
    baseURL     = ReadConfig.getApplicationURL()
    username    = ReadConfig.getUsername()
    password    = ReadConfig.getPassword()
    logs        = LogGen.loggen()
    email       = "indrakurniawan@ggmail.com"
    password    = "password"
    firstname   = "Indra"
    lastname    = "kurniawan"
    gender      = "Male" # Male / Female
    dateofbirth = "11/25/2020" # format MM/DD/YYYY
    companyname = "BAGI KOTAK" 
    istaxex     = "Yes" # Yes / No
    newsletter  = ["Your store name","Test store 2"]
    custrole    = ["Forum Moderators","Vendors"] # administrator, Forum Moderators, Guests, Registered, Vendors) 
    mngrvendor  = "Vendor 1" # Not a vendor, Vendor 1, Vendor 2
    active      = "Yes" # Yes / No
    admincomment= "This is admin comment"

    def test_addCustomer(self,setup):
        self.logs.info("***** Test_003_Login *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        
        # Login Step
        self.logs.info("***** Start Login *****")
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logs.info("***** Login successfuly *****")
        
        # Menu Step
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickoncustomermenu()
        self.addCust.clickoncustomermenuitem()
        self.addCust.clickonaddnew()
        self.addCust.setemail(self.email)
        self.addCust.setpassword(self.password)
        self.addCust.setfirstname(self.firstname)
        self.addCust.setlastname(self.lastname)
        self.addCust.setgender(self.gender)
        self.addCust.setdateofbirth(self.dateofbirth)
        self.addCust.setcompanyname(self.companyname)
        self.addCust.setistaxempty(self.istaxex)
        self.addCust.setnewsletter(self.newsletter)
        self.addCust.setcustomerroles(self.custrole)
        self.addCust.setmanageofvendor(self.mngrvendor)
        self.addCust.setactive(self.active)
        self.addCust.setadmincomment(self.admincomment)
        
        self.logs.info("***** End Of Login DDT Test Passed *****")
        self.logs.info("***** Complete Of Login DDT Test Passed *****")

        