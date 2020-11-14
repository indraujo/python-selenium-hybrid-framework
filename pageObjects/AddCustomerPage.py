import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddCustomer:
    link_customer_menu_xpath  = "//a[@href='#']//span[contains(text(),'Customers')]"
    link_customer_menuitem_xpath = "//body/div[3]/div[2]/div[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/span[1]"
    btn_addnew_xpath = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    
    text_email_id = "Email"
    text_password_id = "Password"
    text_firstname_id = "FirstName"
    text_lastname_id = "LastName"
    rb_malegender_id = "Gender_Male"
    rb_femalegender_id = "Gender_Female"
    text_dateofbirth_id = "DateOfBirth"
    text_companyname_id = "Company"
    check_istaxempty_id = "IsTaxExempt"
    textbox_newsletter_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div"
    lstitem_yoursn_xpath    = "//li[contains(text(),'Your store name')]"
    lstitem_teststore_xpath = "//li[contains(text(),'Test store 2')]"
    textbox_customerrole_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    listitem_administrators_xpath = "//li[contains(text(),'Administrators')]"
    listitem_forummoderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    listitem_guest_xpath = "//li[contains(text(),'Guests')]"
    listitem_registered_xpath = "//li[contains(text(),'Registered')]"
    listitem_vendor_xpath = "//li[contains(text(),'Vendors')]"
    drop_managevendor_id = "VendorId"
    check_active_id = "Active"
    text_admincomment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"
    btn_savecontinue_xpath = "//button[@name='save-continue']"

    def __init__(self,driver):
        self.driver = driver

    def clickoncustomermenu(self):
        self.driver.find_element(By.XPATH,self.link_customer_menu_xpath).click()

    def clickoncustomermenuitem(self):
        self.driver.find_element(By.XPATH,self.link_customer_menuitem_xpath).click()

    def clickonaddnew(self):
        self.driver.find_element(By.XPATH,self.btn_addnew_xpath).click()

    def setemail(self,email):
        self.driver.find_element(By.ID,self.text_email_id).clear()
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.text_password_id).clear
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def setfirstname(self,firstname):
        self.driver.find_element(By.ID,self.text_firstname_id).clear()
        self.driver.find_element(By.ID,self.text_firstname_id).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element(By.ID,self.text_lastname_id).clear()
        self.driver.find_element(By.ID,self.text_lastname_id).send_keys(lastname)

    def setgender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rb_malegender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.rb_femalegender_id).click()
        else:
            self.driver.find_element(By.ID,self.rb_malegender_id).click()


    def setdateofbirth(self,dob):
        self.driver.find_element(By.ID,self.text_dateofbirth_id).clear()
        self.driver.find_element(By.ID,self.text_dateofbirth_id).send_keys(dob)

    def setcompanyname(self,companyname):
        self.driver.find_element(By.ID,self.text_companyname_id).clear()
        self.driver.find_element(By.ID,self.text_companyname_id).send_keys(companyname)

    def setistaxempty(self,istax):
        if istax == "No":
            pass
        elif istax == "Yes":
            self.driver.find_element(By.ID,self.check_istaxempty_id).click()
        else:
            pass

    def setnewsletter(self,newsletter):
        for news in newsletter:
            self.driver.find_element(By.XPATH,self.textbox_newsletter_xpath).click()
            time.sleep(2)
            if news == "Your store name":
                self.driver.find_element(By.XPATH,self.lstitem_yoursn_xpath).click()
                time.sleep(2)

            elif news =="Test store 2":
                self.driver.find_element(By.XPATH,self.lstitem_teststore_xpath).click()

    def setcustomerroles(self,roles):
        for role in roles:
            print(role)
            
            time.sleep(1)                       
            self.driver.find_element(By.XPATH,self.textbox_customerrole_xpath).click()
            time.sleep(2)
            if role == "Registered":
                pass # cz Registered is default
                # self.listitem = self.driver.find_element(By.XPATH,self.listitem_registered_xpath).click()
            elif role == "Administrators":
                self.listitem = self.driver.find_element(By.XPATH,self.listitem_administrators_xpath).click()
            elif role == "Guest":
                # Here user can be Registered(or) Guest only one
                self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds']/option[4]").click()
                self.driver.find_element(By.XPATH,self.listitem_guest_xpath).click()
            elif role == "Vendors":
                self.listitem = self.driver.find_element(By.XPATH,self.listitem_vendor_xpath).click()
            elif role == "Forum Moderators":
                self.listitem = self.driver.find_element(By.XPATH,self.listitem_forummoderators_xpath).click()
            else:
                self.listitem = self.driver.find_element(By.XPATH,self.listitem_guest_xpath).click()
            #self.driver.execute_script("arguments[0].click();",self.listitem)
            
    def setmanageofvendor(self,value):
        drp = Select(self.driver.find_element(By.ID,self.drop_managevendor_id))
        drp.select_by_visible_text(value)
     
    def setactive(self,active):
        if active == "No":
            self.driver.find_element(By.ID,self.check_active_id)
        else:
            pass

    def setadmincomment(self,comment):
        self.driver.find_element(By.ID,self.text_admincomment_id).clear()
        self.driver.find_element(By.ID,self.text_admincomment_id).send_keys(comment)

    def clickbuttonsave(self):
        self.driver.find_element(By.ID,self.btn_save_xpath)

    def clickbuttonsavecontinue(self):
        self.driver.find_element(By.ID,self.btn_savecontinue_xpath)