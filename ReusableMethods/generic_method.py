from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Elements.ProductTypeElement import ProductTypeElements
import random
import string


def select_product(context, product):
    if product == 'admin':
        context.driver.find_element(By.XPATH, ProductTypeElements.admin_product).click()


def get_element_text(context, element):
    return context.driver.find_element(By.XPATH, element).text


def click_button(context, expression):
    locator_types = [By.ID, By.XPATH, By.NAME]
    for locator_type in locator_types:
        try:
            context.driver.find_element(locator_type, expression).click()
            break  # Break the loop if the element is found and clicked
        except NoSuchElementException:
            print(f"Element not found with {locator_type}: {expression}")

    context.driver.find_element(By.XPATH, expression).click()


def generate_random_string(length=8, prefix=""):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return prefix + random_string
