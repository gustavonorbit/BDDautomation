from Base import startBrowser
from behave import *
from Library import ConfigReader
from Page import RegistrationPage

driver = startBrowser.start_browser()
register = RegistrationPage.RegistrationClass(driver)

@given(u'User is on Registrattion page')
def step_impl(context):
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    context.driver = driver
    assert "Login" in driver.title, "Título da página não corresponde"


@when(u'User enter username')
def step_impl(context):
    register.enter_username("teste")
     


@when(u'User enter password')
def step_impl(context):
    register.enter_password("pass123")
     


@when(u'User click on signup button')
def step_impl(context):
    register.click_sign()    


@then(u'User should be registered successfully')
def step_impl(context):
    print("User registered successfully")
    