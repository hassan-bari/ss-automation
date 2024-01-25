from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from GlobalVariables.LoginVariables import *
from Elements.LoginElement import *


def open_url(context):
    context.driver.get(LoginVariable.application_url)
    context.wait = WebDriverWait(context.driver, 10)
    context.wait.until(EC.visibility_of_element_located((By.ID, LoginElement.login_email_textbox)))


def enter_email(context, email):
    context.driver.find_element(By.ID, LoginElement.login_email_textbox).send_keys(email)


def enter_password(context, password):
    context.driver.find_element(By.ID, LoginElement.login_password_textbox).send_keys(password)


def login_click_button(context):
    context.driver.find_element(By.ID, LoginElement.login_button).click()


def login_with_session(context):
    context.wait.until(
        EC.visibility_of_element_located((By.XPATH,LoginElement.login_another_session_title)))
    another_session_page = context.driver.find_element(By.XPATH,
                                                       LoginElement.login_continue_here)
    context.driver.find_element(By.XPATH, LoginElement.login_continue_here).click()
    context.wait.until(EC.visibility_of_element_located((By.XPATH, LoginElement.product_selection_heading)))

def verify_text(context,message):
    assert LoginVariable.product_selection_title in message

