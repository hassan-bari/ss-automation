import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from GlobalVariables.LoginVariables import *
from Elements.LoginElement import *
from Elements.ProductTypeElement import  *



def navigate_to_product_type_management(context):
        context.driver.find_element(By.XPATH,ProductTypeElements.platform_admin).click()
        time.sleep(2)
        context.driver.find_element(By.XPATH,ProductTypeElements.product_type).click()

