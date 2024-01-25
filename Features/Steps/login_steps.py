from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from GlobalVariables.LoginVariables import *
from ReusableMethods.LoginMethods import *


@given('the user is on the login page')
def step_user_on_login_page(context):
    open_url(context)


@when('the user enters valid username and password')
def step_user_enters_credentials(context):

    enter_email(context,LoginVariable.login_email_address)
    enter_password(context,LoginVariable.login_password)
    login_click_button(context)


@then('the user should either be successfully logged in or see the another session page')
def step_user_logged_in_or_sees_another_session_page(context):
    try:
        login_with_session(context)
        message = context.driver.find_element(By.XPATH, "//h4[normalize-space()='Product Selection']").text
        verify_text(context,message)


    except:
        # Handle the exception (if needed)
        context.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[normalize-space()='Product Selection']")))
        message = context.driver.find_element(By.XPATH, "//h4[normalize-space()='Product Selection']").text
        verify_text(context,message)



