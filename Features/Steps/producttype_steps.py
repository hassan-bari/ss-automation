# login_steps.py
import time

from selenium.webdriver import ActionChains

from ReusableMethods.generic_method import *
from ReusableMethods.LoginMethods import *
from ReusableMethods.ProductTypeMethod import *
from Elements.ProductTypeElement import *
from GlobalVariables.ProductTypeVariable import *


@when('the admin enters valid username and password')
def step_user_enters_credentials(context):
    enter_email(context, LoginVariable.admin_login_email_address)
    enter_password(context, LoginVariable.admin_login_password)
    login_click_button(context)


@then(u'user chooses Admin from product selection')
def step_impl(context):
    select_product(context, 'admin')
    time.sleep(5)


@given('the user is on the admin panel')
def step_given_user_on_admin_panel(context):
    # Implementation for navigating to the admin panel
    pass


@when('the user clicks on the "Product Types" option in the side menu')
def step_when_user_clicks_product_types(context):
    navigate_to_product_type_management(context)
    time.sleep(5)


@then('the user should be redirected to the "Product Type" page')
def step_then_redirected_to_add_product_type_page(context):
    title = get_element_text(context, ProductTypeElements.product_type_title)
    print(title)
    print(product_type_page_title)
    assert title in product_type_page_title


@then('the user should be redirected to the "Add Product Type" page')
def step_then_redirected_to_add_product_type_page(context):
    title = get_element_text(context, ProductTypeElements.product_type_add_title)
    print(title)
    print(product_type_page_title)
    assert title in product_type_add_title


@when('the user clicks on "Add New Product Type" button')
def step_click_add_new_product_type_button(context):
    time.sleep(5)
    click_button(context, ProductTypeElements.product_type_add_button)
    time.sleep(5)


@when(u'the user add all required fields')
def step_impl(context):
    time.sleep(5)
    context.random_string_with_postfix = generate_random_string(10, "Product")
    context.driver.find_element(By.NAME, ProductTypeElements.product_type_add_name).send_keys(
        context.random_string_with_postfix)
    time.sleep(5)


@when(u'the user clicks on the "Save" button')
def step_impl(context):
    click_button(context, ProductTypeElements.product_type_add_save_btn)
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'fixed top-')]")))


@then(u'the new product type is successfully created')
def step_impl(context):
    pass


@then(u'the user sees a success message confirming the creation')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[contains(@class,'fixed top-')]").text
    assert text in '✔️ Success! Product type created successfully.'


@then(u'the user is able to see the product in listing')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout

    # Explicitly wait for the input element to be present
    input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))

    # Send keys to the input element
    input_element.send_keys(context.random_string_with_postfix)
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout
    tbody_element = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody")))

    # Now you can further interact with the search results in the tbody
    # For example, you can retrieve all rows from the tbody
    rows = tbody_element.find_elements(By.TAG_NAME, "tr")

    # Print the text content of each row
    found = False
    # context.random_string_with_postfix="hassan"
    for row in rows:
        if context.random_string_with_postfix in row.text:
            found = True
            break
    assert found


@when(u'the user selects an added product type from the list')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout

    # Explicitly wait for the input element to be present
    input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))

    # Send keys to the input element
    input_element.send_keys(context.random_string_with_postfix)
    time.sleep(5)
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout
    tbody_element = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody")))

    # Now you can further interact with the search results in the tbody
    # For example, you can retrieve all rows from the tbody
    rows = tbody_element.find_elements(By.TAG_NAME, "tr")

    # Print the text content of each row
    found = False
    # context.random_string_with_postfix="hassan"
    for row in rows:
        if context.random_string_with_postfix in row.text:
            found = True
            break
    assert found


    # Now you can further interact with the search results in the tbody
    # For example, you can retrieve all rows from the tbody
    # rows = tbody_element.find_elements(By.TAG_NAME, "tr")
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout
    action_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='dropdown relative']")))

    # Print the text content of each row
    # context.random_string_with_postfix="hassan"

    for row in rows:
        if context.random_string_with_postfix in row.text:
            # Find the action menu in the row and click it
            row.find_element(By.XPATH, "//*[@class='dropdown relative']").click()  # Replace with the actual class name

            # Assume there is an 'Edit' option in the action menu
            edit_option = context.driver.find_element(By.LINK_TEXT, 'Edit')  # Replace with the actual link text
            edit_option.click()
            break
        # You are now in the edit page for the selected row


@when(u'the user updates the name of the product type')
def step_impl(context):
    time.sleep(5)
    context.random_string_with_postfix_updated = generate_random_string(10, "Updated")
    context.driver.find_element(By.NAME, ProductTypeElements.product_type_edit_name).send_keys(
        context.random_string_with_postfix_updated)
    time.sleep(5)
    context.driver.find_element(By.XPATH,"(//button[normalize-space()='Save & Update'])[1]").click()
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'fixed top-')]")))



@then(u'the product type is successfully updated')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//*[contains(@class,'fixed top-')]").text
    assert text in '🔄 Succes Product type updated successfully.'


@then(u'the user is redirected to the product type listing to see the updated result')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout

    # Explicitly wait for the input element to be present
    input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))

    # Send keys to the input element
    input_element.send_keys(context.random_string_with_postfix_updated)
    time.sleep(5)
    wait = WebDriverWait(context.driver, 10)  # 10 seconds timeout
    tbody_element = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody")))

    # Now you can further interact with the search results in the tbody
    # For example, you can retrieve all rows from the tbody
    rows = tbody_element.find_elements(By.TAG_NAME, "tr")

    # Print the text content of each row
    found = False
    # context.random_string_with_postfix="hassan"
    for row in rows:
        if context.random_string_with_postfix_updated in row.text:
            found = True
            break
    assert found


