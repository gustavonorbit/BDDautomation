from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@given(u'User is on registration page')
def step_impl(context):
    context.options = Options()
    context.options.add_argument("--start-maximized")
    # ...existing code...
    context.options.add_argument("--ignore-certificate-errors")
    context.options.add_argument("--allow-insecure-localhost")
# ...existing code...
    #options.add_argument("--headless")
    context.service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=context.service, options=context.options)
    context.driver.get("https://demoqa.com/automation-practice-form")


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element(By.ID,"firstName").send_keys("teste")
    context.driver.find_element(By.ID,"lastName").send_keys("teste")


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element(By.ID, "userEmail").send_keys("teste@teste.com")
    gender_radio = context.driver.find_element(By.ID, "gender-radio-1")
    context.driver.execute_script("arguments[0].click();", gender_radio)  # Mais robusto que .click()


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element(By.ID,"userNumber").send_keys("61995587068")


@when(u'User Click on signup button')
def step_impl(context):
    submit_btn = context.driver.find_element(By.ID, "submit")
    context.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
    submit_btn.click()


@then(u'User should be registered successfully')
def step_impl(context):
    print("User registered successfully")
    time.sleep(2)  # Wait for 2 seconds to see the result

@when(u'User enters dulicate username')
def step_impl(context):
    print("User enters duplicate username")
