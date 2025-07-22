from Library import ConfigReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RegistrationClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
         driver.find_element(By.NAME,ConfigReader.fetchElementLocators("Registration","username_name")).send_keys(username)

    def enter_email(self, email):
         driver.find_element(By.XPATH,"//input[@name='fld_email']").send_keys(email)

    def enter_password(self, password):
         driver.find_element(By.NAME,"fld_password").send_keys(password)
    
    def enter_cpassword(self, cpassword):
         driver.find_element(By.NAME,ConfigReader.fetchElementLocators('Registration','password_name_c')).send_keys(cpassword)

    def enter_birthday(self, birthday):
         driver.find_element(By.NAME,"dob").send_keys(birthday)

    def click_terms(self):
        driver.find_element(By.NAME,"terms").click()
    
    def enter_phone(self, phone):
         driver.find_element(By.NAME,"phone").send_keys(phone)
    
    def enter_address(self, address):
         driver.find_element(By.NAME,"address").send_keys(address)

    def click_radio_button(self):
         driver.find_element(By.XPATH,"//input[@value='home']").click()
    
    def enter_sex(self, val):
        select_element1 = driver.find_element(By.NAME, "sex")
        select = Select(select_element1)
        select.select_by_value(val)

    def enter_country(self, country):
        select_element2 = driver.find_element(By.NAME,"country")
        select2 = Select(select_element2)
        select2.select_by_value(country)
    
    def enter_state(self, state):
        select_element3 = driver.find_element(By.NAME,"state")
        select3 = Select(select_element3)
        select3.select_by_value(state)
    
    def enter_city(self, city):
        select_element4 = driver.find_element(By.NAME,"city")
        select4 = Select(select_element4)
        select4.select_by_value(city)
    
    def enter_zip(self, zip):
        driver.find_element(By.NAME,"zip").send_keys(zip)
    
    def click_sign(self):
        driver.find_element(By.XPATH,"//input[@value='Sign up']").click()