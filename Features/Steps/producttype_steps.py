# login_steps.py

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ReusableMethods.LoginMethods import *



# @given('the user is on the login page')
# def step_user_on_login_page(context):
#     open_url(context)

@when('the admin enters valid username and password')
def step_user_enters_credentials(context):
    enter_email(context,LoginVariable.admin_login_email_address)
    enter_password(context,LoginVariable.admin_login_password)
    login_click_button(context)


# @then('the user should be successfully logged in')
# def step_user_successfully_logged_in(context):
#
#       try:
#         login_with_session(context)
#         message = context.driver.find_element(By.XPATH, "//h4[normalize-space()='Product Selection']").text
#         verify_text(context,message)
#
#       except:
#         # Handle the exception (if needed)
#         context.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[normalize-space()='Product Selection']")))
#         message = context.driver.find_element(By.XPATH, "//h4[normalize-space()='Product Selection']").text
#         verify_text(context,message)

@given('the user is on the admin panel')
def step_given_user_on_admin_panel(context):
    # Implementation for navigating to the admin panel
    pass

@when('the user clicks on the "Product Types" option in the side menu')
def step_when_user_clicks_product_types(context):
    # Implementation for clicking on "Product Types" in the side menu
    pass

@when('the user clicks on the "Add New" button')
def step_when_user_clicks_add_new(context):
    # Implementation for clicking on "Add New" button
    pass

@then('the user should be redirected to the "Add Product Type" page')
def step_then_redirected_to_add_product_type_page(context):
    # Implementation to check if the user is on the "Add Product Type" page
    pass
